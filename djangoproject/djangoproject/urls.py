from django.contrib import admin
from blogs.views import index
from django.conf.urls import include, url

urlpatterns = [
    
    url(r'^admin/',admin.site.urls),
    url(r'^$',index,name='index'),


]
