from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def home(request):
    gift=MyModel.objects.all()
    return render(request,'home.html',{'gift':gift})

