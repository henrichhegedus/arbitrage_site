from django.shortcuts import render
from .models import Scrape, Arbs
# Create your views here.
from django.http import HttpResponse


def arbs(request):
    data = Arbs.objects.all()
    context = {'data':data}
    return render(request, 'arb_detail.html', context)

def scrape(request):
    data = Scrape.objects.all()
    context = {'data': data}
    return render(request, 'scrape_detail.html', context)

