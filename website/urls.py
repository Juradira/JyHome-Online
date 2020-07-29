from . import views
from django.urls import path

app_name = 'website'
urlpatterns = [
    path('', views.IndexView, name='index_page'),
    path('blog', views.BlogView, name='blog_page'),
]
