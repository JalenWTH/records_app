from django.urls import path

from app_3 import views

urlpatterns = [
    path('home', views.homepage, name='homepage'),
    path('base', views.base, name='base'),
    path('<str:firstname>/record', views.record, name='record')

]