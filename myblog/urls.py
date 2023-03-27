from django.urls import path
from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.home , name='home'),
    path('ip/', views.ipAddr , name='ip'),

]