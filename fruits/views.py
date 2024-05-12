from django.shortcuts import render

from price.models import Fruit #type: ignore

def home(request):
    fruits=Fruit.objects.all()
    context={
        'fruits':fruits,
    }
    return render(request,'home.html',context)
