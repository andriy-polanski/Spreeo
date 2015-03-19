# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'reflex_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255, null=True, db_index=True)),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Photo'])

        # Adding model 'ProductVariantType'
        db.create_table(u'reflex_productvarianttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_variant_types', to=orm['reflex.Product'])),
            ('variant_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_variant_types', to=orm['reflex.VariantType'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductVariantType'])

        # Adding model 'TargetedUser'
        db.create_table(u'reflex_targeteduser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('broadcast_request', self.gf('django.db.models.fields.related.ForeignKey')(related_name='targeted_users', to=orm['reflex.Campaign'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_campaigns', to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['TargetedUser'])

        # Adding model 'SkuPrice'
        db.create_table(u'reflex_skuprice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('django.db.models.fields.related.ForeignKey')(related_name='price', to=orm['reflex.ProductSku'])),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('sale_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=2, blank=True)),
            ('on_sale', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['SkuPrice'])

        # Adding model 'Campaign'
        db.create_table(u'reflex_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='campaigns', to=orm['reflex.Merchant'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.TopLevelCategory'], null=True, blank=True)),
            ('broadcast_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('promotional_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('listing_page_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('from_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('till_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('display_style', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='campaign_locations', null=True, to=orm['reflex.Location'])),
            ('terms_and_conditions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('active_request', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='current_requests', null=True, to=orm['reflex.BroadcastRequest'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Campaign'])

        # Adding model 'Comment'
        db.create_table(u'reflex_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Comment'])

        # Adding model 'ProductCategoryHeading'
        db.create_table(u'reflex_productcategoryheading', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='headings', to=orm['reflex.ProductCategory'])),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('data_type', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductCategoryHeading'])

        # Adding model 'VariantType'
        db.create_table(u'reflex_varianttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='variant_types', to=orm['reflex.Merchant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['VariantType'])

        # Adding unique constraint on 'VariantType', fields ['merchant', 'name']
        db.create_unique(u'reflex_varianttype', ['merchant_id', 'name'])

        # Adding model 'TopLevelCategory'
        db.create_table(u'reflex_toplevelcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['TopLevelCategory'])

        # Adding model 'Follower'
        db.create_table(u'reflex_follower', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.Merchant'])),
            ('unfollowed', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Follower'])

        # Adding model 'MerchantGenericPage'
        db.create_table(u'reflex_merchantgenericpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='generic_pages', to=orm['reflex.Merchant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantGenericPage'])

        # Adding unique constraint on 'MerchantGenericPage', fields ['merchant', 'name']
        db.create_unique(u'reflex_merchantgenericpage', ['merchant_id', 'name'])

        # Adding model 'MerchantContact'
        db.create_table(u'reflex_merchantcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contacts', to=orm['reflex.Merchant'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=6, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantContact'])

        # Adding model 'BroadcastRequest'
        db.create_table(u'reflex_broadcastrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(related_name='broadcast_requests', to=orm['reflex.Campaign'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('status_reason', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['BroadcastRequest'])

        # Adding model 'CartItem'
        db.create_table(u'reflex_cartitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['reflex.Cart'])),
            ('sku', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cart_items', null=True, to=orm['reflex.ProductSku'])),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['CartItem'])

        # Adding unique constraint on 'CartItem', fields ['cart', 'sku']
        db.create_unique(u'reflex_cartitem', ['cart_id', 'sku_id'])

        # Adding model 'TemplateImage'
        db.create_table(u'reflex_templateimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.Merchant'])),
            ('image_file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255, null=True, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_template_images', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'reflex', ['TemplateImage'])

        # Adding model 'MerchantMolGateway'
        db.create_table(u'reflex_merchantmolgateway', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='gateways', to=orm['reflex.Merchant'])),
            ('mol_merchant_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('mol_vkey', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantMolGateway'])

        # Adding model 'Shared'
        db.create_table(u'reflex_shared', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('preview_text', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('preview_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('shared_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shared', to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Shared'])

        # Adding model 'Location'
        db.create_table(u'reflex_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='locations', to=orm['reflex.Merchant'])),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(default='0', null=True, max_digits=9, decimal_places=6, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(default='0', null=True, max_digits=9, decimal_places=6, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Location'])

        # Adding model 'Specification'
        db.create_table(u'reflex_specification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specifications', to=orm['reflex.Product'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('category_heading', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.ProductCategoryHeading'], null=True, blank=True)),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('data_type', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Specification'])

        # Adding model 'Friend'
        db.create_table(u'reflex_friend', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='friends', to=orm['auth.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='followers', to=orm['auth.User'])),
            ('reciprocated', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Friend'])

        # Adding model 'ProductStatus'
        db.create_table(u'reflex_productstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', to=orm['reflex.Product'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', to=orm['reflex.Location'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(related_name='statuses', to=orm['reflex.ProductStatusValue'])),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')()),
            ('valid_till', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductStatus'])

        # Adding model 'MerchantCoupon'
        db.create_table(u'reflex_merchantcoupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='coupons', to=orm['reflex.Merchant'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('coupon_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('coupon_product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.Product'], null=True, blank=True)),
            ('coupon_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.StoreLevelCategory'], null=True, blank=True)),
            ('coupon_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('coupon_min_purchase', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=2, blank=True)),
            ('discount_type', self.gf('django.db.models.fields.IntegerField')()),
            ('coupon_value', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=11, decimal_places=2, blank=True)),
            ('coupon_limit_per_user', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
            ('valid_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('valid_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantCoupon'])

        # Adding unique constraint on 'MerchantCoupon', fields ['merchant', 'code']
        db.create_unique(u'reflex_merchantcoupon', ['merchant_id', 'code'])

        # Adding model 'MerchantSpecification'
        db.create_table(u'reflex_merchantspecification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='specifications', to=orm['reflex.Merchant'])),
            ('heading', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('data_type', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'reflex', ['MerchantSpecification'])

        # Adding model 'ProductSkuAttr'
        db.create_table(u'reflex_productskuattr', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product_sku', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attrs', to=orm['reflex.ProductSku'])),
            ('variant_value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.VariantValue'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductSkuAttr'])

        # Adding model 'UserView'
        db.create_table(u'reflex_userview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_views', to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('referral_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_views_referral', to=orm['contenttypes.ContentType'])),
            ('referral_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['UserView'])

        # Adding model 'FeedItem'
        db.create_table(u'reflex_feeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('from_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('till_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2030, 1, 1, 0, 0))),
            ('for_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='feed_items', null=True, to=orm['auth.User'])),
            ('self_post', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['FeedItem'])

        # Adding model 'CampaignProduct'
        db.create_table(u'reflex_campaignproduct', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['reflex.Campaign'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='in_campaigns', to=orm['reflex.Product'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['CampaignProduct'])

        # Adding model 'StockImage'
        db.create_table(u'reflex_stockimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255, null=True, db_index=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['StockImage'])

        # Adding model 'Cart'
        db.create_table(u'reflex_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carts', to=orm['reflex.Merchant'])),
            ('sessionid', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='carts', null=True, to=orm['auth.User'])),
            ('special_instructions', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Cart'])

        # Adding unique constraint on 'Cart', fields ['merchant', 'sessionid']
        db.create_unique(u'reflex_cart', ['merchant_id', 'sessionid'])

        # Adding model 'Product'
        db.create_table(u'reflex_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=125, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['reflex.ProductCategory'])),
            ('tag', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=255, blank=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['reflex.Merchant'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('store_category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='products', null=True, to=orm['reflex.StoreLevelCategory'])),
            ('promo_sticker', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('is_merchant_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_editor_featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visibility', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('schedule_publish', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Product'])

        # Adding model 'UserProfile'
        db.create_table(u'reflex_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['auth.User'])),
            ('avatar', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['UserProfile'])

        # Adding model 'Merchant'
        db.create_table(u'reflex_merchant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120, db_index=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.TopLevelCategory'])),
            ('logo', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('on_demand_create', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'reflex', ['Merchant'])

        # Adding model 'MerchantUser'
        db.create_table(u'reflex_merchantuser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='merchant_users', to=orm['reflex.Merchant'])),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='merchant_user', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'reflex', ['MerchantUser'])

        # Adding model 'ProductStatusValue'
        db.create_table(u'reflex_productstatusvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status_text', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('sentiment', self.gf('django.db.models.fields.IntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductStatusValue'])

        # Adding model 'ProductImage'
        db.create_table(u'reflex_productimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['reflex.Product'])),
            ('default_scale_type', self.gf('django.db.models.fields.IntegerField')(default=3)),
            ('image_file', self.gf('sorl.thumbnail.fields.ImageField')(max_length=255)),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='product_images', null=True, to=orm['reflex.Photo'])),
            ('is_primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'reflex', ['ProductImage'])

        # Adding model 'CartCoupon'
        db.create_table(u'reflex_cartcoupon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(related_name='coupons', to=orm['reflex.Cart'])),
            ('coupon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.MerchantCoupon'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['CartCoupon'])

        # Adding model 'MerchantImage'
        db.create_table(u'reflex_merchantimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['reflex.Merchant'])),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'reflex', ['MerchantImage'])

        # Adding model 'ProductCategory'
        db.create_table(u'reflex_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductCategory'])

        # Adding model 'MerchantNote'
        db.create_table(u'reflex_merchantnote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notes', to=orm['reflex.Merchant'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'reflex', ['MerchantNote'])

        # Adding model 'AlternateIdentifier'
        db.create_table(u'reflex_alternateidentifier', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.Merchant'])),
            ('id_type', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal(u'reflex', ['AlternateIdentifier'])

        # Adding model 'VariantValue'
        db.create_table(u'reflex_variantvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variant_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='variant_values', to=orm['reflex.VariantType'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['VariantValue'])

        # Adding unique constraint on 'VariantValue', fields ['variant_type', 'value']
        db.create_unique(u'reflex_variantvalue', ['variant_type_id', 'value'])

        # Adding model 'Favorite'
        db.create_table(u'reflex_favorite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('preview_text', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('preview_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Favorite'])

        # Adding model 'MerchantPromotionItem'
        db.create_table(u'reflex_merchantpromotionitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('promotion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['reflex.MerchantPromotion'])),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.Merchant'])),
        ))
        db.send_create_signal(u'reflex', ['MerchantPromotionItem'])

        # Adding model 'StoreLevelCategory'
        db.create_table(u'reflex_storelevelcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_level_categories', to=orm['reflex.Merchant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='store_level_categories', to=orm['reflex.TopLevelCategory'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['StoreLevelCategory'])

        # Adding model 'WebsiteTemplate'
        db.create_table(u'reflex_websitetemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.OneToOneField')(related_name='template', unique=True, to=orm['reflex.Merchant'])),
            ('json', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='created_templates', to=orm['auth.User'])),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('updated_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='updated_templates', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'reflex', ['WebsiteTemplate'])

        # Adding model 'MerchantPromotion'
        db.create_table(u'reflex_merchantpromotion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.TopLevelCategory'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantPromotion'])

        # Adding model 'Editorial'
        db.create_table(u'reflex_editorial', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.OneToOneField')(related_name='editorial', unique=True, to=orm['flatpages.FlatPage'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('teaser_text', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('teaser_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('published_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['Editorial'])

        # Adding model 'MerchantShippingOption'
        db.create_table(u'reflex_merchantshippingoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('merchant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shipping_options', to=orm['reflex.Merchant'])),
            ('rate_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rate_value', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['MerchantShippingOption'])

        # Adding model 'ProductSku'
        db.create_table(u'reflex_productsku', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='skus', to=orm['reflex.Product'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=13, db_index=True)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('avail_from', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('avail_to', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('order_priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'reflex', ['ProductSku'])


    def backwards(self, orm):
        # Removing unique constraint on 'VariantValue', fields ['variant_type', 'value']
        db.delete_unique(u'reflex_variantvalue', ['variant_type_id', 'value'])

        # Removing unique constraint on 'Cart', fields ['merchant', 'sessionid']
        db.delete_unique(u'reflex_cart', ['merchant_id', 'sessionid'])

        # Removing unique constraint on 'MerchantCoupon', fields ['merchant', 'code']
        db.delete_unique(u'reflex_merchantcoupon', ['merchant_id', 'code'])

        # Removing unique constraint on 'CartItem', fields ['cart', 'sku']
        db.delete_unique(u'reflex_cartitem', ['cart_id', 'sku_id'])

        # Removing unique constraint on 'MerchantGenericPage', fields ['merchant', 'name']
        db.delete_unique(u'reflex_merchantgenericpage', ['merchant_id', 'name'])

        # Removing unique constraint on 'VariantType', fields ['merchant', 'name']
        db.delete_unique(u'reflex_varianttype', ['merchant_id', 'name'])

        # Deleting model 'Photo'
        db.delete_table(u'reflex_photo')

        # Deleting model 'ProductVariantType'
        db.delete_table(u'reflex_productvarianttype')

        # Deleting model 'TargetedUser'
        db.delete_table(u'reflex_targeteduser')

        # Deleting model 'SkuPrice'
        db.delete_table(u'reflex_skuprice')

        # Deleting model 'Campaign'
        db.delete_table(u'reflex_campaign')

        # Deleting model 'Comment'
        db.delete_table(u'reflex_comment')

        # Deleting model 'ProductCategoryHeading'
        db.delete_table(u'reflex_productcategoryheading')

        # Deleting model 'VariantType'
        db.delete_table(u'reflex_varianttype')

        # Deleting model 'TopLevelCategory'
        db.delete_table(u'reflex_toplevelcategory')

        # Deleting model 'Follower'
        db.delete_table(u'reflex_follower')

        # Deleting model 'MerchantGenericPage'
        db.delete_table(u'reflex_merchantgenericpage')

        # Deleting model 'MerchantContact'
        db.delete_table(u'reflex_merchantcontact')

        # Deleting model 'BroadcastRequest'
        db.delete_table(u'reflex_broadcastrequest')

        # Deleting model 'CartItem'
        db.delete_table(u'reflex_cartitem')

        # Deleting model 'TemplateImage'
        db.delete_table(u'reflex_templateimage')

        # Deleting model 'MerchantMolGateway'
        db.delete_table(u'reflex_merchantmolgateway')

        # Deleting model 'Shared'
        db.delete_table(u'reflex_shared')

        # Deleting model 'Location'
        db.delete_table(u'reflex_location')

        # Deleting model 'Specification'
        db.delete_table(u'reflex_specification')

        # Deleting model 'Friend'
        db.delete_table(u'reflex_friend')

        # Deleting model 'ProductStatus'
        db.delete_table(u'reflex_productstatus')

        # Deleting model 'MerchantCoupon'
        db.delete_table(u'reflex_merchantcoupon')

        # Deleting model 'MerchantSpecification'
        db.delete_table(u'reflex_merchantspecification')

        # Deleting model 'ProductSkuAttr'
        db.delete_table(u'reflex_productskuattr')

        # Deleting model 'UserView'
        db.delete_table(u'reflex_userview')

        # Deleting model 'FeedItem'
        db.delete_table(u'reflex_feeditem')

        # Deleting model 'CampaignProduct'
        db.delete_table(u'reflex_campaignproduct')

        # Deleting model 'StockImage'
        db.delete_table(u'reflex_stockimage')

        # Deleting model 'Cart'
        db.delete_table(u'reflex_cart')

        # Deleting model 'Product'
        db.delete_table(u'reflex_product')

        # Deleting model 'UserProfile'
        db.delete_table(u'reflex_userprofile')

        # Deleting model 'Merchant'
        db.delete_table(u'reflex_merchant')

        # Deleting model 'MerchantUser'
        db.delete_table(u'reflex_merchantuser')

        # Deleting model 'ProductStatusValue'
        db.delete_table(u'reflex_productstatusvalue')

        # Deleting model 'ProductImage'
        db.delete_table(u'reflex_productimage')

        # Deleting model 'CartCoupon'
        db.delete_table(u'reflex_cartcoupon')

        # Deleting model 'MerchantImage'
        db.delete_table(u'reflex_merchantimage')

        # Deleting model 'ProductCategory'
        db.delete_table(u'reflex_productcategory')

        # Deleting model 'MerchantNote'
        db.delete_table(u'reflex_merchantnote')

        # Deleting model 'AlternateIdentifier'
        db.delete_table(u'reflex_alternateidentifier')

        # Deleting model 'VariantValue'
        db.delete_table(u'reflex_variantvalue')

        # Deleting model 'Favorite'
        db.delete_table(u'reflex_favorite')

        # Deleting model 'MerchantPromotionItem'
        db.delete_table(u'reflex_merchantpromotionitem')

        # Deleting model 'StoreLevelCategory'
        db.delete_table(u'reflex_storelevelcategory')

        # Deleting model 'WebsiteTemplate'
        db.delete_table(u'reflex_websitetemplate')

        # Deleting model 'MerchantPromotion'
        db.delete_table(u'reflex_merchantpromotion')

        # Deleting model 'Editorial'
        db.delete_table(u'reflex_editorial')

        # Deleting model 'MerchantShippingOption'
        db.delete_table(u'reflex_merchantshippingoption')

        # Deleting model 'ProductSku'
        db.delete_table(u'reflex_productsku')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'flatpages.flatpage': {
            'Meta': {'ordering': "(u'url',)", 'object_name': 'FlatPage', 'db_table': "u'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        u'reflex.alternateidentifier': {
            'Meta': {'object_name': 'AlternateIdentifier'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_type': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.Merchant']"}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        u'reflex.broadcastrequest': {
            'Meta': {'object_name': 'BroadcastRequest'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'broadcast_requests'", 'to': u"orm['reflex.Campaign']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'status_reason': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'active_request': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'current_requests'", 'null': 'True', 'to': u"orm['reflex.BroadcastRequest']"}),
            'broadcast_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.TopLevelCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_style': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'from_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing_page_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'campaign_locations'", 'null': 'True', 'to': u"orm['reflex.Location']"}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'campaigns'", 'to': u"orm['reflex.Merchant']"}),
            'promotional_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'terms_and_conditions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'till_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.campaignproduct': {
            'Meta': {'object_name': 'CampaignProduct'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['reflex.Campaign']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_campaigns'", 'to': u"orm['reflex.Product']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.cart': {
            'Meta': {'unique_together': "(('merchant', 'sessionid'),)", 'object_name': 'Cart'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carts'", 'to': u"orm['reflex.Merchant']"}),
            'sessionid': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'special_instructions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'carts'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'reflex.cartcoupon': {
            'Meta': {'object_name': 'CartCoupon'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'coupons'", 'to': u"orm['reflex.Cart']"}),
            'coupon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.MerchantCoupon']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.cartitem': {
            'Meta': {'unique_together': "(('cart', 'sku'),)", 'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['reflex.Cart']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart_items'", 'null': 'True', 'to': u"orm['reflex.ProductSku']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.comment': {
            'Meta': {'object_name': 'Comment'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reflex.editorial': {
            'Meta': {'object_name': 'Editorial'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'editorial'", 'unique': 'True', 'to': u"orm['flatpages.FlatPage']"}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'teaser_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'teaser_text': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.favorite': {
            'Meta': {'object_name': 'Favorite'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'preview_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'preview_text': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reflex.feeditem': {
            'Meta': {'object_name': 'FeedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'for_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'feed_items'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'from_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'self_post': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'till_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2030, 1, 1, 0, 0)'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.follower': {
            'Meta': {'object_name': 'Follower'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.Merchant']"}),
            'unfollowed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'reflex.friend': {
            'Meta': {'object_name': 'Friend'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'followers'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reciprocated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'friends'", 'to': u"orm['auth.User']"})
        },
        u'reflex.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'to': u"orm['reflex.Merchant']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchant': {
            'Meta': {'object_name': 'Merchant'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.TopLevelCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
            'on_demand_create': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchantcontact': {
            'Meta': {'object_name': 'MerchantContact'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['reflex.Merchant']"}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'reflex.merchantcoupon': {
            'Meta': {'unique_together': "(('merchant', 'code'),)", 'object_name': 'MerchantCoupon'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'coupon_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.StoreLevelCategory']", 'null': 'True', 'blank': 'True'}),
            'coupon_limit_per_user': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'coupon_min_purchase': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'coupon_product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.Product']", 'null': 'True', 'blank': 'True'}),
            'coupon_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'coupon_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'coupon_value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'discount_type': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'coupons'", 'to': u"orm['reflex.Merchant']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'valid_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reflex.merchantgenericpage': {
            'Meta': {'unique_together': "(('merchant', 'name'),)", 'object_name': 'MerchantGenericPage'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'generic_pages'", 'to': u"orm['reflex.Merchant']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchantimage': {
            'Meta': {'object_name': 'MerchantImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['reflex.Merchant']"})
        },
        u'reflex.merchantmolgateway': {
            'Meta': {'object_name': 'MerchantMolGateway'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gateways'", 'to': u"orm['reflex.Merchant']"}),
            'mol_merchant_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'mol_vkey': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchantnote': {
            'Meta': {'object_name': 'MerchantNote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': u"orm['reflex.Merchant']"}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'reflex.merchantpromotion': {
            'Meta': {'object_name': 'MerchantPromotion'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.TopLevelCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchantpromotionitem': {
            'Meta': {'object_name': 'MerchantPromotionItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.Merchant']"}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['reflex.MerchantPromotion']"})
        },
        u'reflex.merchantshippingoption': {
            'Meta': {'object_name': 'MerchantShippingOption'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shipping_options'", 'to': u"orm['reflex.Merchant']"}),
            'rate_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rate_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.merchantspecification': {
            'Meta': {'object_name': 'MerchantSpecification'},
            'data_type': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specifications'", 'to': u"orm['reflex.Merchant']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'reflex.merchantuser': {
            'Meta': {'object_name': 'MerchantUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'merchant_users'", 'to': u"orm['reflex.Merchant']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'merchant_user'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'reflex.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'})
        },
        u'reflex.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['reflex.ProductCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_editor_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_merchant_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': u"orm['reflex.Merchant']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'order_priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'promo_sticker': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'published_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'schedule_publish': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'store_category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': u"orm['reflex.StoreLevelCategory']"}),
            'tag': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'visibility': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'reflex.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.productcategoryheading': {
            'Meta': {'object_name': 'ProductCategoryHeading'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'headings'", 'to': u"orm['reflex.ProductCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_type': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.productimage': {
            'Meta': {'object_name': 'ProductImage'},
            'default_scale_type': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255'}),
            'is_primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'product_images'", 'null': 'True', 'to': u"orm['reflex.Photo']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['reflex.Product']"})
        },
        u'reflex.productsku': {
            'Meta': {'object_name': 'ProductSku'},
            'avail_from': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'avail_to': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '13', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'skus'", 'to': u"orm['reflex.Product']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.productskuattr': {
            'Meta': {'object_name': 'ProductSkuAttr'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_sku': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attrs'", 'to': u"orm['reflex.ProductSku']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'variant_value': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.VariantValue']"})
        },
        u'reflex.productstatus': {
            'Meta': {'object_name': 'ProductStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['reflex.Location']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['reflex.Product']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'statuses'", 'to': u"orm['reflex.ProductStatusValue']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'valid_from': ('django.db.models.fields.DateTimeField', [], {}),
            'valid_till': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'reflex.productstatusvalue': {
            'Meta': {'object_name': 'ProductStatusValue'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentiment': ('django.db.models.fields.IntegerField', [], {}),
            'status_text': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.productvarianttype': {
            'Meta': {'object_name': 'ProductVariantType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_variant_types'", 'to': u"orm['reflex.Product']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'variant_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_variant_types'", 'to': u"orm['reflex.VariantType']"})
        },
        u'reflex.shared': {
            'Meta': {'object_name': 'Shared'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'preview_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'preview_text': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'shared_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shared'", 'to': u"orm['auth.User']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.skuprice': {
            'Meta': {'object_name': 'SkuPrice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_sale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'sale_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'price'", 'to': u"orm['reflex.ProductSku']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.specification': {
            'Meta': {'object_name': 'Specification'},
            'category_heading': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.ProductCategoryHeading']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_type': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'heading': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'specifications'", 'to': u"orm['reflex.Product']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'reflex.stockimage': {
            'Meta': {'object_name': 'StockImage'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'})
        },
        u'reflex.storelevelcategory': {
            'Meta': {'object_name': 'StoreLevelCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_level_categories'", 'to': u"orm['reflex.Merchant']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'store_level_categories'", 'to': u"orm['reflex.TopLevelCategory']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.targeteduser': {
            'Meta': {'object_name': 'TargetedUser'},
            'broadcast_request': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'targeted_users'", 'to': u"orm['reflex.Campaign']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'in_campaigns'", 'to': u"orm['auth.User']"})
        },
        u'reflex.templateimage': {
            'Meta': {'object_name': 'TemplateImage'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_template_images'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_file': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '255', 'null': 'True', 'db_index': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reflex.Merchant']"})
        },
        u'reflex.toplevelcategory': {
            'Meta': {'object_name': 'TopLevelCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'reflex.userview': {
            'Meta': {'object_name': 'UserView'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_views'", 'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'referral_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_views_referral'", 'to': u"orm['contenttypes.ContentType']"}),
            'referral_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.varianttype': {
            'Meta': {'unique_together': "(('merchant', 'name'),)", 'object_name': 'VariantType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'merchant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'variant_types'", 'to': u"orm['reflex.Merchant']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'reflex.variantvalue': {
            'Meta': {'unique_together': "(('variant_type', 'value'),)", 'object_name': 'VariantValue'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'variant_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'variant_values'", 'to': u"orm['reflex.VariantType']"})
        },
        u'reflex.websitetemplate': {
            'Meta': {'object_name': 'WebsiteTemplate'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_templates'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'json': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'merchant': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'template'", 'unique': 'True', 'to': u"orm['reflex.Merchant']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'updated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'updated_templates'", 'to': u"orm['auth.User']"})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['reflex']