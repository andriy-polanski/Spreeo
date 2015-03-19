from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from reflex.models import *

class MerchantShippingOptionForm(forms.ModelForm):
    
    class Meta:
        model = MerchantShippingOption
        fields = ['rate_name', 'rate_value', 'shipping_region']


@login_required
def shipping_options(request):
    d = {}
    d["shipping_options"] = request.user.merchant_user.merchant.shipping_options.all()
    return render(request, "dashboard/shipping/list.html", d)

@login_required
def edit_shipping_option(request, pk=None):
    d = {}
    merchant = request.user.merchant_user.merchant
    if pk:
        instance = get_object_or_404(MerchantShippingOption, merchant=merchant, id=pk)
    else:
        instance = None
   
    if request.method == "GET":
        d["form"] = form = MerchantShippingOptionForm(instance=instance)
        
    elif request.method == "POST":
        d["form"] = form = MerchantShippingOptionForm(request.POST, instance=instance)
        if form.is_valid():
            if form.has_changed():
                instance = form.save(commit=False)
                new = True if not instance.id else False
                instance.merchant = merchant
                instance.save()
                if new:
                    messages.success(request, "'%s' added" % instance.rate_name)
                else:
                    messages.success(request, "'%s' updated" % instance.rate_name)                   
            else:
                messages.info(request, "'%s' unchanged" % instance.rate_name)
            return HttpResponseRedirect(reverse("dashboard:shipping_options"))

    return render(request, "dashboard/shipping/edit.html", d)

@login_required
def delete_shipping_option(request, pk=None):
    d = {}
    merchant = request.user.merchant_user.merchant
    if pk:
        instance = get_object_or_404(MerchantShippingOption, merchant=merchant, id=pk)
    else:
        instance = None
    d["instance"] = instance
    
    if request.method == "GET":
        return render(request, "dashboard/shipping/delete.html", d)
    elif request.method == "POST":
        rate_name = instance.rate_name
        instance.delete()
        messages.success(request, "'%s' deleted" % rate_name)
        return HttpResponseRedirect(reverse("dashboard:shipping_options"))
