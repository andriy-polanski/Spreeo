from django import forms
from django.forms.models import *
from django.core.urlresolvers import reverse

from reflex.models import *

merchant_profile_fields = fields_for_model(MerchantProfile)

class MerchantProfileForm(forms.ModelForm):

    class Meta:
        model = MerchantProfile
        fields = ['company_name', 'company_short_description',
                  'company_description', 'company_registration_no',
                  'slug', 'category', 'logo']


CONTACT_TYPE_TO_FIELDS = {
    CONTACT_TYPE_PHONE: ["phone"],
    CONTACT_TYPE_EMAIL: ["email"],
    CONTACT_TYPE_URL: ["url"],
    CONTACT_TYPE_ADDRESS: ["address1", "address2", "address3", "city_town", "district", "postcode", "state", "country"],
    CONTACT_TYPE_OTHER: ["other"],
    CONTACT_TYPE_FACEBOOK: ["url"],
    CONTACT_TYPE_BLOG: ["url"]
}

ALL_CONTACT_FIELDS = ["phone", "email", "url", "address1", "address2", "address3", "city_town", "district", "postcode",
                       "state", "country", "other"]

class MerchantContactForm(forms.ModelForm):
    to_delete = forms.BooleanField(required=False)
    label = forms.CharField(max_length=50, required=True)

    def __init__(self, *args, **kwargs):
        super(MerchantContactForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            del self.fields['type']
        else:
            del self.fields['to_delete']

    class Meta:
        model = MerchantContact
        exclude = ('merchant', 'created', 'updated')


