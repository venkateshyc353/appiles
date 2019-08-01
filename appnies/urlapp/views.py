from django.shortcuts import render
from . models import  url_model
from rest_framework import viewsets
from . forms import  url_forms
from .restend import rest_api
# Create your views here.
def url_view(request):
    data=url_model.objects.all()
    return render(request,'testapp/urls.html',{'data':data})


class rest_api_crud(viewsets.ModelViewSet):
    queryset = url_model.objects.all()
    serializer_class = rest_api

def back_view(request):
    return render(request,'testapp/back.html')

def url_post_data(request):
    formm=url_forms()
    if request.method=='POST':
        formm=url_forms(request.POST)
        if formm.is_valid():
            formm.save()
            return url_view(request)
    return render(request,'testapp/fost.html',{'formm':formm})