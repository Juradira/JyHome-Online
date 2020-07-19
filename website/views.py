from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    context = { }
    return render(request, 'website/index.html', context)
