
from django.conf.urls.static import static, serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import handler404
from apps.views import Error404View


urlpatterns = [
   re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
   re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
   path('admin/', admin.site.urls),
   path('', include("apps.urls")),
   path('', include("news.urls")),
   path('users/', include("users.urls")),
   path('contacts/', include("contacts.urls")),
]  
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    

# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = Error404View.as_view()