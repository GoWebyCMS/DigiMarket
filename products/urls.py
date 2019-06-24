from django.conf.urls import include, url

from products.views import ProductListView, ProductDetailView

urlpatterns = [
    url(r'^product/new/$', 'products.views.product_create', name='product_create'),
    url(r'^product/(?P<slug>[\w-]+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^product/(?P<slug>[\w-]+)/edit/$', 'products.views.product_edit', name='product_edit'),
    url(r'^products/$', ProductListView.as_view(), name='product_list'),
]
