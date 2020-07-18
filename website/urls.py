from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView, name='index_page'),
]
