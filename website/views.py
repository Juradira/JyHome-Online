from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def IndexView(request):
    context = { }
    return render(request, 'website/index.html', context)


def BlogView(request):
    user = User.objects.filter(user_name='Lin Jingyi')[0]
    context = {
        'user': user,
    }
    return render(request, 'website/blog.html', context)
