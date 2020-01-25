
from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('act/', views.act, name='act'),

]