from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from reflex.models import *

class MerchantMolGatewayForm(forms.ModelForm):

    class Meta:
        model = MerchantMolGateway
        fields = ['mol_merchant_id', 'mol_vkey']


@login_required
def edit_payment_gateway(request):
    d = {}
    merchant = request.user.merchant_user.merchant
    merchant_mol_gateway = MerchantMolGateway.objects.filter(merchant=merchant).first()

    errors_found = False
    if request.method == "GET":
        d["mol_gateway_form"] = mol_gateway_form = MerchantMolGatewayForm(instance=merchant_mol_gateway)
    elif request.method == "POST":
        d["mol_gateway_form"] = mol_gateway_form = MerchantMolGatewayForm(request.POST, request.FILES, 
                                                                          instance=merchant_mol_gateway) 
        if mol_gateway_form.is_valid() and mol_gateway_form.has_changed():
            merchant_mol_gateway = mol_gateway_form.save(commit=False)
            merchant_mol_gateway.merchant = merchant
            merchant_mol_gateway.save()
        elif not mol_gateway_form.is_valid():
            errors_found = True

        if not errors_found:
            messages.success(request, _('Payment gateway information updated.'))
            return HttpResponseRedirect(reverse("dashboard:edit_payment_gateway"))

    d["errors_found"] = errors_found
    return render(request, "dashboard/payment_gateway/edit.html", d)
