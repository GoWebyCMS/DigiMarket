from django.conf.urls import include, url

urlpatterns = [
    url(r'^detail/(?P<slug>[\w-]+)/$', 'products.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/edit/$', 'products.views.edit_view', name='edit_view'),
    url(r'^list/', 'products.views.list_view', name='list_view'),
    url(r'^create/', 'products.views.create_view', name='create_view'),
]
