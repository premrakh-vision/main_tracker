
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from myapp.views import *
from django.views.static import serve 



route=DefaultRouter()
route.register('data',ScreenShotView,basename='data')
route.register('user',UserView,basename='user')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls)),
    path('view_screen',view_screen,name='view_screen'),
    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

