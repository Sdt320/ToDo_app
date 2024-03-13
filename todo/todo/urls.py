from django.contrib import admin
from django.url import path,include
from django.conf import settings
from django.conf.url.static import static

urlpatterns =[
    path('admin/',admin.site.urls),
    path('',include('user_module.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    