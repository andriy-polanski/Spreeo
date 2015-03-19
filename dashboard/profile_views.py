from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.base import TemplateView

from profile_forms import *

@login_required
def edit_profile(request):
    d = {"CONTACT_TYPE_PHONE": CONTACT_TYPE_PHONE, "CONTACT_TYPE_EMAIL": CONTACT_TYPE_EMAIL,
         "CONTACT_TYPE_URL": CONTACT_TYPE_URL, "CONTACT_TYPE_ADDRESS": CONTACT_TYPE_ADDRESS,
         "CONTACT_TYPE_OTHER": CONTACT_TYPE_OTHER, "CONTACT_TYPE_FACEBOOK": CONTACT_TYPE_FACEBOOK,
         "CONTACT_TYPE_BLOG": CONTACT_TYPE_BLOG}

    merchant = request.user.merchant_user.merchant
    if hasattr(merchant, "merchant_profile"):
        d["merchant_profile"] = merchant_profile = merchant.merchant_profile
    else:
        d["merchant_profile"] = merchant_profile = None

    d["contact_forms"] = contact_forms = []

    errors_found = False

    if request.method == "GET":
        d["profile_form"] = profile_form = MerchantProfileForm(instance=merchant_profile)
        for contact in merchant.contacts.all():
            form = MerchantContactForm(instance=contact, prefix="contact-" + str(contact.id))
            contact_forms.append(form)

    elif request.method == "POST":
        d["profile_form"] = profile_form = MerchantProfileForm(request.POST, request.FILES, instance=merchant_profile)
        if profile_form.is_valid() and profile_form.has_changed():
            merchant_profile = profile_form.save(commit=False)
            merchant_profile.merchant = merchant
            merchant_profile.save()
        elif not profile_form.is_valid():
            errors_found = True

        if request.POST.get('blank-type'):
            new_contact_form = MerchantContactForm(request.POST, prefix='blank')
            if new_contact_form.is_valid():
                instance = new_contact_form.save(commit=False)
                instance.merchant = merchant
                instance.save()
            else:
                errors_found = True
                d["blank_contact_form"] = new_contact_form

        for contact in merchant.contacts.all():
            if request.POST.has_key("contact-%d-label" % contact.id):
                contact_form = MerchantContactForm(request.POST, instance=contact, prefix="contact-" + str(contact.id))
                to_delete_field = contact_form.fields['to_delete']
                data = to_delete_field.widget.value_from_datadict(contact_form.data, contact_form.files,
                                                                  contact_form.add_prefix('to_delete'))
                if to_delete_field.clean(data):
                    contact.delete()
                    continue 
                if contact_form.has_changed():
                    if contact_form.is_valid():
                        instance = contact_form.save(commit=False)
                        instance.save()
                    else:
                        errors_found = True
                contact_forms.append(contact_form)

        if not errors_found:
            return HttpResponseRedirect(reverse("dashboard:edit_profile"))

    d["errors_found"] = errors_found
    if not "blank_contact_form" in d:
        d["blank_contact_form"] = MerchantContactForm(prefix="blank")

    return render(request, "dashboard/profiles/edit_profile.html", d)

