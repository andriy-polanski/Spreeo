from django.conf.urls import patterns, include, url
from dashboard import views

from payment_gateway_views import *
from profile_views import *
from store_category_views import *
from shipping_views import *

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login$', views.dashboard_login_page, name='dashboard_login'),
    url(r'^logout$', views.dashboard_logout, name='dashboard_logout'),
    url(r'^products$', views.ProductListView.as_view(), name='product_list'),
    url(r'^product/edit/(?P<pk>\d+)/$', views.ProductUpdateCreateView.as_view(), name='product_edit'),
    url(r'^product/new/$', views.ProductUpdateCreateView.as_view(), name='product_new'),
    url(r'^product/delete/(?P<pk>\d+)/$', views.ProductDeleteView.as_view(), name='product_delete'),
    url(r'^profile/edit$', edit_profile, name="edit_profile"),
    url(r'^payment_gateway/edit$', edit_payment_gateway, name="edit_payment_gateway"),
    
    url(r'^store_categories$', store_categories, name="store_categories"),
    url(r'^store_category/edit/(?P<pk>\d+)/$', edit_store_category, name='edit_store_category'),
    url(r'^store_category/delete/(?P<pk>\d+)/$', delete_store_category, name='delete_store_category'),
    url(r'^store_category/new/$', edit_store_category, name='new_store_category'),

    url(r'^shipping_options$', shipping_options, name="shipping_options"),
    url(r'^shipping_option/edit/(?P<pk>\d+)/$', edit_shipping_option, name='edit_shipping_option'),
    url(r'^shipping_option/delete/(?P<pk>\d+)/$', delete_shipping_option, name='delete_shipping_option'),
    url(r'^shipping_option/new/$', edit_shipping_option, name='new_shipping_option'),
)


