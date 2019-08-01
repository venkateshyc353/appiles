from django.urls import path,include
from rest_framework import  routers
from . import views
var=routers.DefaultRouter()
var.register('urlapp',views.rest_api_crud)
urlpatterns=[
    path('endapi',include(var.urls)),
    path('post',views.url_post_data),
    path('dataview',views.url_view)

]