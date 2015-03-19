import cgi

from django.contrib import admin
from django.core.urlresolvers import resolve, reverse

from models import *

class ProductImageInline(admin.TabularInline):
    model = ProductImage


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'merchant_link', 'category', 'tag', 'has_images')
    search_fields = ('name', 'merchant__name')
    inlines = [ProductImageInline]

    def has_images(self, obj):
        return len(obj.images.all()) != 0
    has_images.boolean = True

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
            obj.published_date = datetime.now()
        super(ProductAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "merchant":
            kwargs["queryset"] = Merchant.objects.order_by('name')
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return ('created_by', 'published_date')
        else:
            return ('created_by',)

    def merchant_link(self, obj):
        content_type = ContentType.objects.get_for_model(obj.merchant.__class__)
        url = reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model), args=(obj.merchant.id,))
        return '<a href="%s">%s</a>' % (cgi.escape(url, True), cgi.escape(obj.merchant.name, True))

    merchant_link.allow_tags = True
    merchant_link.short_description = "Merchant"


class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class MerchantUserAdmin(admin.ModelAdmin):
    list_display = ('merchant', 'user')


class TopLevelCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(StoreLevelCategory)
admin.site.register(TopLevelCategory, TopLevelCategoryAdmin)
admin.site.register(MerchantUser, MerchantUserAdmin)
admin.site.register(ProductSku)
admin.site.register(ProductSkuAttr)
admin.site.register(ProductVariantType)
admin.site.register(VariantType)
admin.site.register(VariantValue)
