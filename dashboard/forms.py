from django import forms
from django.core import exceptions
from django.shortcuts import get_object_or_404
from django.forms.models import inlineformset_factory
from reflex.models import Product, ProductImage, ProductSku, SkuPrice, ProductSkuAttr, VariantValue, VariantType

from dashboard.widgets import  ImageInput
from bootstrap3_datetime.widgets import DateTimePicker

def _attr_text_field(attribute):
    return forms.CharField(label=attribute.name,
                           required=attribute.required)


def _attr_textarea_field(attribute):
    return forms.CharField(label=attribute.name,
                           widget=forms.Textarea(),
                           required=attribute.required)


def _attr_integer_field(attribute):
    return forms.IntegerField(label=attribute.name,
                              required=attribute.required)


def _attr_boolean_field(attribute):
    return forms.BooleanField(label=attribute.name,
                              required=attribute.required)


def _attr_float_field(attribute):
    return forms.FloatField(label=attribute.name,
                            required=attribute.required)


def _attr_date_field(attribute):
    return forms.DateField(label=attribute.name,
                           required=attribute.required,
                           widget=forms.widgets.DateInput)


def _attr_option_field(attribute):
    return forms.ModelChoiceField(
        label=attribute.name,
        required=attribute.required,
        queryset=attribute.option_group.options.all())


def _attr_multi_option_field(attribute):
    return forms.ModelMultipleChoiceField(
        label=attribute.name,
        required=attribute.required,
        queryset=attribute.option_group.options.all())


def _attr_entity_field(attribute):
    return None


def _attr_numeric_field(attribute):
    return forms.FloatField(label=attribute.name,
                            required=attribute.required)


def _attr_file_field(attribute):
    return forms.FileField(
        label=attribute.name, required=attribute.required)


def _attr_image_field(attribute):
    return forms.ImageField(
        label=attribute.name, required=attribute.required)


class ProductImageForm(forms.ModelForm):
    
    class Meta:
        model = ProductImage
        fields = ['image_file', 'is_primary']
        widgets = {
            'image_file': ImageInput(),
        }

    def save(self, *args, **kwargs):
        # We infer the display order of the image based on the order of the
        # image fields within the formset.
        kwargs['commit'] = False
        obj = super(ProductImageForm, self).save(*args, **kwargs)
        obj.display_order = self.get_display_order()
        obj.save()
        return obj

    def get_display_order(self):
        return self.prefix.split('-').pop()


BaseProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm, extra=2)

class ProductImageFormSet(BaseProductImageFormSet):

    def __init__(self, user, *args, **kwargs):
        super(ProductImageFormSet, self).__init__(*args, **kwargs)


class ProductForm(forms.ModelForm):
    FIELD_FACTORIES = {
        "text": _attr_text_field,
        "richtext": _attr_textarea_field,
        "integer": _attr_integer_field,
        "boolean": _attr_boolean_field,
        "float": _attr_float_field,
        "date": _attr_date_field,
        "option": _attr_option_field,
        "multi_option": _attr_multi_option_field,
        "entity": _attr_entity_field,
        "numeric": _attr_numeric_field,
        "file": _attr_file_field,
        "image": _attr_image_field,
    }

    class Meta:
        model = Product
        fields = [
            'name', 'description', 'unit', 'store_category', 'promo_sticker', 'is_merchant_featured', 'order_priority', 'visibility']

    def __init__(self, merchant, created_by, data=None, *args, **kwargs):
        super(ProductForm, self).__init__(data, *args, **kwargs)
        self.instance.merchant = merchant
        self.instance.created_by = created_by


class SkupriceRecordForm(forms.ModelForm):

    def __init__(self, sku, *args, **kwargs):
        super(SkupriceRecordForm, self).__init__(*args, **kwargs)
        self.instance.sku = sku

    class Meta:
        model = SkuPrice
        fields = ["retail_price", "sale_price", "on_sale"]

        widgets = {
            "retail_price": forms.NumberInput(attrs={"style":"text-align:right", "min": "1.00", "max":"999999.99"}),
            "sale_price": forms.NumberInput(attrs={"style":"text-align:right", "min": "1.00", "max":"999999.99" })
        }

class SkuRecordForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SkuRecordForm, self).__init__(*args, **kwargs)
        try:
            self.skuprice_object = SkuPrice.objects.get(sku=self.instance.pk)
        except Exception as e:
            self.skuprice_object = None

        self.skuprice_form = SkupriceRecordForm(self.instance, instance=self.skuprice_object, prefix=self.prefix)
        self.extra_sku_attributes = {}

    def is_valid(self):
        valid = super(SkuRecordForm, self).is_valid()
        if not self.skuprice_object is None:
            self.skuprice_form = SkupriceRecordForm(self.instance, self.data, {}, instance=self.skuprice_object, prefix=self.prefix)
            valid = valid & self.skuprice_form.is_valid()
        else:
            self.skuprice_form = SkupriceRecordForm(self.instance, self.data, {}, prefix=self.prefix)
            valid = valid & self.skuprice_form.is_valid()

        if (self.data['extra_sku_attributes']):
            self.extra_sku_attributes = extra_sku_attributes = {}
            for attribute_name in self.data['extra_sku_attributes'].split(","):
                extra_sku_attributes[attribute_name] = self.data[self.prefix + "-" + attribute_name]
        
        return valid

    def save(self, commit=True, *args, **kwargs):
        # Commit appears to be False when the product is created and True when the product is updated
        print "Commit:", commit
        save_result = super(SkuRecordForm, self).save(commit=True)
        if not self.skuprice_object is None:
            self.skuprice_form.save(commit=True)
        else:
            sku_price = self.skuprice_form.save(commit=False)
            sku_price.sku = save_result
            sku_price.save()

        merchant = save_result.product.merchant
        for attr, value in self.get_extra_sku_attributes().items():
            try:
                variant_value = VariantValue.objects.get(variant_type__merchant=merchant, variant_type__name=attr, value=value)
            except VariantValue.DoesNotExist:
                print "Creating VariantValue: %s - %s" % (attr, value)
                variant_type = VariantType.objects.get(merchant=merchant, name=attr)
                variant_value = VariantValue(variant_type=variant_type, value=value)
                variant_value.save()
            try:
                product_sku_attr = save_result.attrs.get(variant_value__variant_type__name=attr)
            except ProductSkuAttr.DoesNotExist:
                print "ProductSkuAttr does not exist: %s - %s" % (attr, value)
                product_sku_attr = ProductSkuAttr(product_sku=save_result)
            if not product_sku_attr.pk or product_sku_attr.variant_value != variant_value:
                print "ProductSkuAttr changed or new"
                product_sku_attr.variant_value = variant_value
                product_sku_attr.save()
            else:
                print "ProductSkuAttr unchanged"
        return save_result

    def get_extra_sku_attributes(self):
        if self.extra_sku_attributes:
            print "Reading SKU attributes from form"
            return self.extra_sku_attributes
        else:
            print "Reading SKU attributes from database"
            d = {}
            for attr in self.instance.attrs.all():
                d[attr.variant_value.variant_type.name] = attr.variant_value.value
            return d 
    

    def has_changed(self):
        if not self.skuprice_object is None:
            return True
        return super(SkuRecordForm, self).has_changed()

    class Meta:
        model = ProductSku
        fields = [
            'code', 'quantity'
        ]
        widgets = {
            "quantity": forms.NumberInput(attrs={"style":"text-align:right", "min": "0", "max": "9999999"}),
            "code": forms.TextInput(attrs={"size": "10"})
        }

BaseSkuRecordFormSet = inlineformset_factory(
    Product, ProductSku, form=SkuRecordForm, extra=1)

class SkuRecordFormSet(BaseSkuRecordFormSet):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SkuRecordFormSet, self).__init__(*args, **kwargs)

    def _construct_form(self, i, **kwargs):
        kwargs['user'] = self.user
        return super(SkuRecordFormSet, self)._construct_form(
            i, **kwargs)

    def save(self, commit=True):
        super(SkuRecordFormSet, self).save(commit)

    def clean(self):
        super(SkuRecordFormSet, self).clean()

        active_forms = []
        for form in self.initial_forms:
            if not form in self.deleted_forms:
                active_forms.append(form)

        for form in self.extra_forms:
            if form.has_changed() and not self._should_delete_form(form):
                active_forms.append(form)


        if len(active_forms) < 1:
            raise forms.ValidationError("At least one SKU row must exist.")

        extra_sku_attributes_group = []

        for form in active_forms:
            extra_attributes = form.get_extra_sku_attributes()
            if any([cmp(extra_attributes, v) == 0 for v in extra_sku_attributes_group]):
                raise forms.ValidationError("Duplicate rows with same extra SKU attribute values exist.")
            else:
                extra_sku_attributes_group.append(extra_attributes)
