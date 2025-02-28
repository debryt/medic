
from django.contrib import admin
from django.urls import path
from mediapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
]
