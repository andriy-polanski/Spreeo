from datetime import datetime
import os

from django.core.files import File
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.utils import formats
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from sorl.thumbnail import ImageField

DATA_TYPE_INTEGER = 1
DATA_TYPE_DECIMAL = 2
DATA_TYPE_TEXT    = 3
DATA_TYPE_HTML    = 4

DATA_TYPE_CHOICES = (
    (DATA_TYPE_INTEGER, 'Integer'),
    (DATA_TYPE_DECIMAL, 'Decimal'),
    (DATA_TYPE_TEXT, 'Text'),
    (DATA_TYPE_HTML, 'HTML'),
)

SENTIMENT_NEUTRAL = 1
SENTIMENT_POSITIVE = 2
SENTIMENT_NEGATIVE = 3

SENTIMENT_CHOICES = (
    (SENTIMENT_NEUTRAL, 'Neutral'),
    (SENTIMENT_POSITIVE, 'Positive'),
    (SENTIMENT_NEGATIVE, 'Negative'),
)

# Taken from 
# http://developer.android.com/reference/android/widget/ImageView.ScaleType.html
SCALE_TYPE_FIT_XY         = 1
SCALE_TYPE_FIT_START      = 2
SCALE_TYPE_FIT_CENTER     = 3
SCALE_TYPE_FIT_END        = 4
SCALE_TYPE_CENTER         = 5
SCALE_TYPE_CENTER_CROP    = 6
SCALE_TYPE_CENTER_INSIDE  = 7

SCALE_TYPE_CHOICES = (
    (SCALE_TYPE_FIT_XY, "Fit XY"),
    (SCALE_TYPE_FIT_START, "Fit Start"),
    (SCALE_TYPE_FIT_CENTER, "Fit Center"),
    (SCALE_TYPE_FIT_END, "Fit End"),
    (SCALE_TYPE_CENTER, "Center"),
    (SCALE_TYPE_CENTER_CROP, "Center Crop"),
    (SCALE_TYPE_CENTER_INSIDE, "Center Inside"),
)

BROADCAST_REQUEST_DRAFT     = 1
BROADCAST_REQUEST_PENDING   = 2
BROADCAST_REQUEST_APPROVED  = 3
BROADCAST_REQUEST_DENIED    = 4
BROADCAST_REQUEST_CANCELLED = 5
BROADCAST_REQUEST_PUBLISHED = 8

# This is implicit, it's never in the database
BROADCAST_REQUEST_ACTIVE = 6
BROADCAST_REQUEST_PREVIOUS = 7

BROADCAST_REQUEST_CHOICES = (
    (BROADCAST_REQUEST_DRAFT, "Draft"),
    (BROADCAST_REQUEST_PENDING, "Pending"),
    (BROADCAST_REQUEST_APPROVED, "Approved"),
    (BROADCAST_REQUEST_DENIED, "Denied"),
    (BROADCAST_REQUEST_CANCELLED, "Cancelled"),
    (BROADCAST_REQUEST_ACTIVE, "Active"),
    (BROADCAST_REQUEST_PREVIOUS, "Previous"),
    (BROADCAST_REQUEST_PUBLISHED, "Published"),
)

BROADCAST_REQUEST_CHOICES_DICT = dict(BROADCAST_REQUEST_CHOICES)

BROADCAST_TYPE_GLOBAL    = 1
BROADCAST_TYPE_TARGETED  = 2

BROADCAST_TYPE_CHOICES = (
    (BROADCAST_TYPE_GLOBAL, "Global"),
    (BROADCAST_TYPE_TARGETED, "Targeted"),
)

CAMPAIGN_DISPLAY_STYLE_LIST = 1
CAMPAIGN_DISPLAY_STYLE_GRID = 2

CAMPAIGN_DISPLAY_STYLE_CHOICES = (
    (CAMPAIGN_DISPLAY_STYLE_LIST, "List"),
    (CAMPAIGN_DISPLAY_STYLE_GRID, "Grid"),
)

EDITORIAL_STATUS_DRAFT = 1
EDITORIAL_STATUS_PUBLISHED = 2

EDITORIAL_STATUS_CHOICES = (
    (EDITORIAL_STATUS_DRAFT, "Draft"),
    (EDITORIAL_STATUS_PUBLISHED, "Published"),
)

MAX_DATE = datetime(2030, 1, 1)

ALTERNATE_ID_TYPE_IC = 1
ALTERNATE_ID_TYPE_CHOICES = (
    (ALTERNATE_ID_TYPE_IC, "IC"),
)

PRODUCT_HIDDEN = 1
PRODUCT_PUBLISHED = 2

PRODUCT_VISIBILITY = (
    (PRODUCT_HIDDEN, "Hidden"),
    (PRODUCT_PUBLISHED, "Published")
)


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    # No longer needed
    price = models.CharField(max_length=125, blank=True, null=True)
    description = models.TextField(blank=True)
    # To be set manually in code based on StoreLevelCategory
    category = models.ForeignKey('reflex.ProductCategory', related_name="products", blank=True, null=True)

    tag = models.CharField(max_length=255, db_index=True, blank=True)

    merchant = models.ForeignKey('reflex.Merchant', related_name="products")
    created_by = models.ForeignKey(User)

    unit = models.CharField(max_length=100, blank=True)

    # The date the product first became visible to the product
    published_date = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    store_category = models.ForeignKey('reflex.StoreLevelCategory', related_name="products", blank=True, null=True)
    promo_sticker = models.CharField(max_length=100, blank=True)
    is_merchant_featured = models.BooleanField(default=False)
    is_editor_featured = models.BooleanField(default=False)
    order_priority = models.IntegerField(default=0)
    visibility = models.IntegerField(choices=PRODUCT_VISIBILITY, default=PRODUCT_PUBLISHED)
    schedule_publish = models.DateTimeField(blank=True, null=True)

    def preview_text(self):
        return self.name

    def preview_image(self):
        images = self.images.all()
        if images.exists():
            return images[0].image_file
        else:
            return None

    def __unicode__(self):
        if hasattr(self, "merchant"):
            return "[" + self.merchant.name + "] " + self.name
        else: 
            return self.name
            

class ProductImage(models.Model):
    product = models.ForeignKey('reflex.Product', related_name="images")
    default_scale_type = models.IntegerField(choices=SCALE_TYPE_CHOICES, 
        default=SCALE_TYPE_FIT_CENTER)
    image_file = ImageField(max_length=255, upload_to="product_images")
    photo = models.ForeignKey('reflex.Photo', related_name="product_images", 
        blank=True, null=True)
    
    is_primary = models.BooleanField(default=False)
    order_priority = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.photo:
            self.image_file = self.photo.image_file
            self.photo.used = True
            self.photo.save()
        super(ProductImage, self).save(*args, **kwargs)


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Product categories'


class ProductCategoryHeading(models.Model):
    category = models.ForeignKey('reflex.ProductCategory', related_name='headings')

    heading = models.CharField(max_length=80, blank=True)
    help_text = models.CharField(max_length=100, blank=True)
    data_type = models.IntegerField(choices=DATA_TYPE_CHOICES, default=DATA_TYPE_TEXT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Specification(models.Model):
    product = models.ForeignKey('reflex.Product', related_name='specifications')

    order = models.IntegerField(blank=True, null=True)

    category_heading = models.ForeignKey('reflex.ProductCategoryHeading', null=True, blank=True)

    heading = models.CharField(max_length=80, blank=True)
    data_type = models.IntegerField(choices=DATA_TYPE_CHOICES, default=DATA_TYPE_TEXT)

    value = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MerchantPromotion(models.Model):
    category = models.ForeignKey('reflex.TopLevelCategory', blank=True, null=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    image = ImageField(upload_to="merchant_promotion_images")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    published_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class MerchantPromotionItem(models.Model):
    promotion = models.ForeignKey('reflex.MerchantPromotion', related_name='items')
    merchant = models.ForeignKey('reflex.Merchant')


class Merchant(models.Model):

    @staticmethod
    def find_by_slug(slug):
        return Merchant.objects.get(id=slug)

    name = models.CharField(max_length=120, db_index=True)

    category = models.ForeignKey('reflex.TopLevelCategory', db_index=True)

    logo = ImageField(upload_to="merchant_logos", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, blank=True, null=True)

    on_demand_create = models.BooleanField(default=False)

    @property
    def slug(self):
        return self.id

    def get_logo(self):
        if self.logo:
            return self.logo.url
        else:
            for product in self.products.all():
                image = product.preview_image() 
                if image:
                    return image.url
        return '/static/icons/default_merchant.png'

    def __unicode__(self):
        return self.name


class MerchantNote(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name="notes") 
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return 'by %s on %s' % (self.created_by, formats.date_format(self.created, "DATETIME_FORMAT"))


class MerchantImage(models.Model):
    merchant = models.ForeignKey(Merchant, related_name="images")
    image = ImageField(upload_to="merchant_images")


class MerchantUser(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='merchant_users')
    user = models.OneToOneField(User, related_name='merchant_user')


class Location(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='locations')
    location_name = models.CharField(max_length=80)

    address = models.CharField(max_length=255)

    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, default="0")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, default="0")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ProductStatus(models.Model):
    product = models.ForeignKey('reflex.Product', related_name='statuses')
    location = models.ForeignKey('reflex.Location', related_name='statuses')

    status = models.ForeignKey('reflex.ProductStatusValue', related_name='statuses')

    valid_from = models.DateTimeField()
    valid_till = models.DateTimeField(null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ProductStatusValue(models.Model):
    status_text = models.CharField(max_length=80) 
    sentiment = models.IntegerField(choices=SENTIMENT_CHOICES)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TopLevelCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Campaign categories'


class Campaign(models.Model):
    title = models.CharField(max_length=120) 
    description = models.TextField(blank=True)

    merchant = models.ForeignKey('reflex.Merchant', related_name='campaigns')

    # This will be set by the administrator.
    category = models.ForeignKey('reflex.TopLevelCategory', blank=True, null=True)

    broadcast_type = models.IntegerField(choices=BROADCAST_TYPE_CHOICES,
            default=BROADCAST_TYPE_GLOBAL)

    # Mandatory when making a broadcast request
    promotional_image = ImageField(upload_to='promotional_images', null=True, blank=True)

    listing_page_image = ImageField(upload_to='listing_page_images', null=True, blank=True)

    # These two values are mandatory when making a broadcast request
    from_date = models.DateTimeField(null=True, blank=True)
    till_date = models.DateTimeField(null=True, blank=True)

    display_style = models.IntegerField(choices=CAMPAIGN_DISPLAY_STYLE_CHOICES, default=CAMPAIGN_DISPLAY_STYLE_GRID)

    location = models.ForeignKey('reflex.Location', related_name='campaign_locations', null=True, blank=True)

    terms_and_conditions = models.TextField(blank=True)

    active_request = models.ForeignKey('reflex.BroadcastRequest', 
            related_name="current_requests", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def preview_text(self):
        return self.title

    def preview_image(self):
        return self.promotional_image

    def status_text(self):
        if not self.active_request:
            return BROADCAST_REQUEST_CHOICES_DICT[BROADCAST_REQUEST_DRAFT]
        elif self.active_request.status ==  BROADCAST_REQUEST_PUBLISHED:
            now = timezone.now()
            if now > self.from_date and now < self.till_date:
                return "Active"
            else:
                return "Previous"
        else:
            return BROADCAST_REQUEST_CHOICES_DICT[self.active_request.status]

    def status_sentiment(self):
        if not self.active_request or self.active_request.status == BROADCAST_REQUEST_DRAFT:
            return ""
        elif self.active_request.status ==  BROADCAST_REQUEST_PUBLISHED:
            now = timezone.now()
            if now > self.from_date and now < self.till_date:
                return "info"
            else:
                return "info"
        elif self.active_request.status == BROADCAST_REQUEST_APPROVED:
            return "success"
        elif self.active_request.status == BROADCAST_REQUEST_CANCELLED:
            return "inverse"
        elif self.active_request.status == BROADCAST_REQUEST_DENIED:
            return "important"
        elif self.active_request.status == BROADCAST_REQUEST_PENDING:
            return "warning"
        else:
            return ""

    def __unicode__(self):
        return self.title;


class CampaignProduct(models.Model):
    campaign = models.ForeignKey('reflex.Campaign', related_name='products')
    product = models.ForeignKey('reflex.Product', related_name='in_campaigns')
    order = models.IntegerField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "Product in campaign - " + self.campaign.title


class BroadcastRequest(models.Model):
    campaign = models.ForeignKey('reflex.Campaign', related_name='broadcast_requests')
    
    status = models.IntegerField(choices=BROADCAST_REQUEST_CHOICES, 
            default=BROADCAST_REQUEST_DRAFT) 

    status_reason = models.CharField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(BroadcastRequest, self).__init__(*args, **kwargs)
        self.prev_status = self.status


class TargetedUser(models.Model):
    broadcast_request = models.ForeignKey('reflex.Campaign', related_name='targeted_users')
    user = models.ForeignKey('auth.User', related_name='in_campaigns')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class FeedItem(models.Model):
    # This can either be: 
    #     - Follower
    #     - Favorite
    #     - Campaign (both global and targeted)
    #     - Shared
    #     - Comment
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    from_date = models.DateTimeField()
    till_date = models.DateTimeField(default=MAX_DATE)
 
    # Empty for global broadcasts
    for_user = models.ForeignKey(User, related_name='feed_items', null=True, blank=True)

    # True if content_object was created by for_user
    self_post = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Shared(models.Model):
    # This can either be:
    #     - Product
    #     - Campaign
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    preview_text = models.CharField(max_length=120)
    preview_image = ImageField(upload_to="shared_images")

    shared_by = models.ForeignKey(User, related_name='shared')

    feed_items = generic.GenericRelation('reflex.FeedItem',
                                         content_type_field='content_type',
                                         object_id_field='object_id')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Follower(models.Model):
    user = models.ForeignKey(User)

    # This can either be Merchant or User
    merchant = models.ForeignKey('reflex.Merchant')

    feed_items = generic.GenericRelation('reflex.FeedItem',
                                         content_type_field='content_type',
                                         object_id_field='object_id')

    unfollowed = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Favorite(models.Model):
    user = models.ForeignKey(User)

    # This can either be Campaign or Product
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    favorited = generic.GenericForeignKey('content_type', 'object_id')

    preview_text = models.CharField(max_length=120)
    preview_image = ImageField(upload_to="favorite_images")

    feed_items = generic.GenericRelation('reflex.FeedItem',
                                         content_type_field='content_type',
                                         object_id_field='object_id')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserView(models.Model):
    # This can either be Campaign or Product
    content_type = models.ForeignKey(ContentType, related_name='user_views')
    object_id = models.PositiveIntegerField()
    viewed = generic.GenericForeignKey('content_type', 'object_id')

    # This can either be Campaign, Merchant (Business page) or Editorial
    referral_content_type = models.ForeignKey(ContentType, related_name='user_views_referral')
    referral_object_id = models.PositiveIntegerField()
    referral = generic.GenericForeignKey('referral_content_type', 'referral_object_id')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Editorial(models.Model):
    page = models.OneToOneField(FlatPage, related_name="editorial")
    status = models.IntegerField(choices=EDITORIAL_STATUS_CHOICES, default=EDITORIAL_STATUS_DRAFT)

    author = models.ForeignKey(User)

    teaser_text = models.TextField(blank=True)
    teaser_image = ImageField(upload_to="editorial_images", blank=True, null=True)

    published_date = models.DateTimeField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.status == EDITORIAL_STATUS_PUBLISHED and not self.published_date: 
            self.published_date = datetime.now()
        super(Editorial, self).save(*args, **kwargs)


class Friend(models.Model):
    user = models.ForeignKey(User, related_name="friends")
    friend = models.ForeignKey(User, related_name="followers")

    reciprocated = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    avatar = ImageField(upload_to="profile_images", blank=True, null=True)
 
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    state    = models.CharField(max_length=255, blank=True)
    country  = models.CharField(max_length=255, blank=True)
 
    @staticmethod
    def create_default_profile(user):
        file_dir = os.path.dirname(os.path.abspath(__file__))
        profile = UserProfile(user=user)
        profile.avatar.save('default_avatar.png', 
                File(open(file_dir + '/static/icons/default_avatar.png')))
        profile.save()
        return profile


class Comment(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User)
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class MerchantSpecification(models.Model):
    merchant = models.ForeignKey(Merchant, related_name="specifications")
    heading = models.CharField(max_length=80)
    data_type = models.IntegerField(choices=DATA_TYPE_CHOICES, default=DATA_TYPE_TEXT)
    value = models.TextField()


class Photo(models.Model):
    image_file = ImageField(max_length=255, upload_to="repository", null=True, db_index=True)
    remarks = models.CharField(max_length=255, blank=True)
    used = models.BooleanField(default=False, db_index=True)
    tag = models.CharField(max_length=255, db_index=True, blank=True)


class WebsiteTemplate(models.Model):
    @staticmethod
    def get_for_merchant(merchant):
        if hasattr(merchant, "template"):
            return merchant.template
        else:
            return None

    @staticmethod
    def get_for_user(user):
        if hasattr(user.merchant_user.merchant, "template"):
            return user.merchant_user.merchant.template
        else:
            return None

    merchant = models.OneToOneField('reflex.Merchant', related_name='template')
    json = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="created_templates")

    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name="updated_templates")


class StockImage(models.Model):
    image_file = ImageField(max_length=255, upload_to="stock_images", null=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)


class TemplateImage(models.Model):
    merchant = models.ForeignKey(Merchant)
    image_file = ImageField(max_length=255, upload_to="template_images", null=True, db_index=True)

    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="created_template_images")


class AlternateIdentifier(models.Model):
    merchant = models.ForeignKey(Merchant)
    id_type = models.IntegerField(choices=ALTERNATE_ID_TYPE_CHOICES, db_index=True)
    value = models.CharField(max_length=50, unique=True, db_index=True)


DISCOUNT_FIXED = 1
DISCOUNT_PERCENTAGE = 2
DISCOUNT_FREE_SHIPPING = 3

DISCOUNT_CHOICES = (
    (DISCOUNT_FIXED, "Fixed"),
    (DISCOUNT_PERCENTAGE, "Percentage"),
    (DISCOUNT_FREE_SHIPPING, "Free Shipping")
)

CONTACT_TYPE_PHONE = 1
CONTACT_TYPE_EMAIL = 2
CONTACT_TYPE_URL = 3
CONTACT_TYPE_ADDRESS = 4
CONTACT_TYPE_OTHER = 5
CONTACT_TYPE_FACEBOOK = 6
CONTACT_TYPE_BLOG = 7

CONTACT_TYPE_CHOICES = (
    (CONTACT_TYPE_PHONE, "Phone"),
    (CONTACT_TYPE_EMAIL, "Email"),
    (CONTACT_TYPE_URL, "URL"),
    (CONTACT_TYPE_ADDRESS, "Address"),
    (CONTACT_TYPE_OTHER, "Other"), 
    (CONTACT_TYPE_FACEBOOK, "Facebook"),
    (CONTACT_TYPE_BLOG, "Blog"),
)

COUPON_TYPE_STORE_WIDE = 1
COUPON_TYPE_PRODUCT = 2
COUPON_TYPE_CATEGORY = 3
COUPON_TYPE_USER = 4
COUPON_TYPE_PURCHASE = 5

COUPON_TYPE_CHOICES = (
    (COUPON_TYPE_STORE_WIDE, "Store Wide"),
    (COUPON_TYPE_PRODUCT, "Product"),
    (COUPON_TYPE_CATEGORY, "Category"),
    (COUPON_TYPE_USER, "User"),
    (COUPON_TYPE_PURCHASE, "Minimum Purchase")
)

ORDER_PENDING = 1
ORDER_PROCESSING = 2
ORDER_DELIVERED = 3
ORDER_REFUNDED = 4
ORDER_CANCELED = 5
ORDER_FAILED = 6
ORDER_PAYMENT_FAILED = 7
ORDER_PAYMENT_SUCCESSFUL = 8

ORDER_STATUS_CHOICES = (
    (ORDER_PENDING, "Pending"),
    (ORDER_PAYMENT_FAILED, "Payment Failed"),
    (ORDER_PAYMENT_SUCCESSFUL, "Payment Successful"),
    (ORDER_PROCESSING, "Processing"),
    (ORDER_DELIVERED, "Delivered"),
    (ORDER_REFUNDED, "Refunded"),
    (ORDER_CANCELED, "Canceled"),
    (ORDER_FAILED, "Failed delivery")
)


class MerchantContact(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='contacts')
    type = models.IntegerField(choices=CONTACT_TYPE_CHOICES)
    label = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    url = models.URLField(max_length=255, blank=True)
    other = models.TextField(blank=True)
    
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    city_town = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=255, blank=True)
    state    = models.CharField(max_length=255, blank=True)
    country  = models.CharField(max_length=255, blank=True)
    
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class MerchantMolGateway(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='gateways')
    
    mol_merchant_id = models.CharField(max_length=50, blank=True)
    mol_vkey = models.CharField(max_length=100, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

SHIPPING_REGION_MALAYSIA_WIDE = 1
SHIPPING_REGION_MALAYSIA_WEST = 2
SHIPPING_REGION_MALAYSIA_EAST = 3

SHIPPING_REGION_OPTIONS = (
    (SHIPPING_REGION_MALAYSIA_WIDE, "Malaysia Wide"),
    (SHIPPING_REGION_MALAYSIA_EAST, "West Malaysia"),
    (SHIPPING_REGION_MALAYSIA_WEST, "East Malaysia"),
)

SHIPPING_REGION_OPTIONS_DICT = dict(SHIPPING_REGION_OPTIONS)

class MerchantShippingOption(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='shipping_options')

    rate_name = models.CharField(max_length=50)
    rate_value = models.DecimalField(max_digits=11, decimal_places=2)
    
    shipping_region = models.IntegerField(choices=SHIPPING_REGION_OPTIONS, default=SHIPPING_REGION_MALAYSIA_WIDE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def shipping_region_text(self):
        return SHIPPING_REGION_OPTIONS_DICT[self.shipping_region]

class VariantType(models.Model):  
    merchant = models.ForeignKey('reflex.Merchant', related_name='variant_types')
    name = models.CharField(max_length=100, db_index=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
       unique_together = ('merchant', 'name')
        
    def __unicode__(self):
        return "%s: %s" % (self.merchant.name, self.name)


class ProductVariantType(models.Model):  
    product = models.ForeignKey('reflex.Product', related_name='product_variant_types')
    variant_type = models.ForeignKey('reflex.VariantType', related_name='product_variant_types')

    # May need to store order_priority here in the future    

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class VariantValue(models.Model):
    variant_type = models.ForeignKey('reflex.VariantType', related_name='variant_values')
    value = models.CharField(max_length=100, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('variant_type', 'value')

    def __unicode__(self):
        return "%s - %s" % (unicode(self.variant_type), self.value)


class ProductSku(models.Model):
    product = models.ForeignKey('reflex.Product', related_name='skus')

    # Save code must check whether there are two SKUs from the same merchant with identical SKU codes
    code = models.CharField(max_length=13, blank=False, db_index=True)
    quantity = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(9999999)
    ])
    avail_from = models.DateTimeField(blank=True, null=True)
    avail_to = models.DateTimeField(blank=True, null=True)
    order_priority = models.IntegerField(blank=False, null=False, default=0)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s [%s]" % (self.product, self.code)

class ProductSkuAttr(models.Model):
    product_sku = models.ForeignKey('reflex.ProductSku', related_name='attrs')
    variant_value = models.ForeignKey('reflex.VariantValue')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Must manually check in code whether there are two SKUs with identical sets of attributes
   
        
class SkuPrice(models.Model): 
    sku = models.ForeignKey('reflex.ProductSku', related_name='price')
    retail_price = models.DecimalField(max_digits=11, decimal_places=2)
    sale_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    on_sale = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
class MerchantCoupon(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='coupons')
    code = models.CharField(max_length=20, blank=False, db_index=True)
    coupon_type = models.IntegerField(choices=COUPON_TYPE_CHOICES, 
            default=COUPON_TYPE_STORE_WIDE)
    
    coupon_product = models.ForeignKey("reflex.Product", blank=True, null=True)
    coupon_category = models.ForeignKey("reflex.StoreLevelCategory", blank=True, null=True)
    coupon_user = models.ForeignKey("auth.User", blank=True, null=True)
    coupon_min_purchase = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    discount_type = models.IntegerField(choices=DISCOUNT_CHOICES)
    # Empty if it is free shippping
    coupon_value = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)

    coupon_limit_per_user = models.IntegerField(blank=True, null=True, default=1)
    
    valid_from = models.DateTimeField(blank=True, null=True)
    valid_to = models.DateTimeField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('merchant', 'code')


class Cart(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='carts')
    sessionid = models.CharField(max_length=64, blank=True)
    user = models.ForeignKey('auth.User', related_name='carts', blank=True, null=True)

    special_instructions = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('merchant', 'sessionid')

    def __unicode__(self):
        return "%s [%s] - %s" % (self.user, self.sessionid, self.merchant)


class CartItem(models.Model):
    cart = models.ForeignKey('reflex.Cart', related_name='items')
    sku = models.ForeignKey('reflex.ProductSku', blank=True, null=True, related_name='cart_items')
    quantity = models.PositiveIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('cart', 'sku')

    def __unicode__(self):
        return "%d - %d" % (self.id, self.quantity)

class CartCoupon(models.Model):
    cart = models.ForeignKey('reflex.Cart', related_name='coupons')
    coupon = models.ForeignKey('reflex.MerchantCoupon')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class StoreLevelCategory(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='store_level_categories')
    name = models.CharField(max_length=100, db_index=True)
    path = models.CharField(max_length=100, db_index=True, null=True)

    parent = models.ForeignKey('reflex.TopLevelCategory', related_name='store_level_categories')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s - %s" % (self.merchant.name, self.name)

    class Meta:
        verbose_name_plural = "Store level categories"


class MerchantGenericPage(models.Model):
    merchant = models.ForeignKey('reflex.Merchant', related_name='generic_pages')
    name = models.CharField(max_length=100, blank=False, db_index=True)
    content = models.TextField(blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("merchant", "name")


class MerchantProfile(models.Model):
    merchant = models.OneToOneField('reflex.Merchant', related_name="merchant_profile")

    company_name = models.CharField(max_length=120, db_index=True)
    company_short_description = models.CharField(max_length=80, blank=True)
    company_description = models.TextField(blank=True)
    company_registration_no = models.CharField(max_length=20, blank=True)

    slug = models.SlugField(verbose_name="Shop URL", max_length=50, db_index=True)

    category = models.ForeignKey('reflex.TopLevelCategory', db_index=True, blank=True, null=True)
    logo = ImageField(upload_to="merchant_logos", blank=True, null=True)

    created_by = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

