# -*- encoding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/', include('hotelurbano.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^prod_images/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.PROD_IMAGES,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
