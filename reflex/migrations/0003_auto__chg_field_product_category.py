# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.category'
        db.alter_column(u'reflex_product', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['reflex.ProductCategory']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Product.category'
        raise RuntimeError("Cannot reverse this migration. 'Product.category' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Product.category'
        db.alter_column(u'reflex_product', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reflex.ProductCategory']))

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
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'products'", 'null': 'True', 'to': u"orm['reflex.ProductCategory']"}),
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