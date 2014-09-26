from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('social.urls')),
                       url(r'^api-auth/', include('rest_framework.urls',
                           namespace='rest_framework'))
                       url(r'^activity/', include('actstream.urls')),
                       url(r'^d3jsdemo/', include('d3jsdemo.urls')),
                       )


if settings.DEVELOPMENT:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.views.static',
                            url(r'^media/(?P<path>.*)$', 'serve',
                                {'document_root': settings.MEDIA_ROOT}),
                            )

 # Debug Toolbar
    if settings.DEBUG:
        import debug_toolbar
        urlpatterns += patterns('',
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )