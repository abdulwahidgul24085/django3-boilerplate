from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('users/', include('users.urls', namespace='users')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib import admin
    import debug_toolbar
    urlpatterns += [
        path('admin/', admin.site.urls,),
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
