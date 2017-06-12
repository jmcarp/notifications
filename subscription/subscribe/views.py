from django.shortcuts import render
from django.http import HttpResponse
from subscribe.forms import SubscribeForm 

def subscribes(request):
    form_class = SubscribeForm
    
    return render(request, 'subscribe.html', {
        'form': form_class,
    })

def index(request):
    return HttpResponse("Subcribe to Open States!!!!!")