from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='indexPage'),
    url(r'^projects/(\d+)',views.project,name ='projects'),
