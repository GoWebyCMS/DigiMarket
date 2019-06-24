from django.conf.urls import include, url

urlpatterns = [
    url(r'^product/(?P<slug>[\w-]+)$', 'products.views.product_detail', name='product_detail'),
    url(r'^product/(?P<slug>[\w-]+)/edit$', 'products.views.product_edit', name='product_edit'),
    url(r'^products$', 'products.views.product_list', name='product_list'),
    url(r'^product/create$', 'products.views.product_create', name='product_create'),
]
