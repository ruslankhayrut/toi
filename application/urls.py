
from django.urls import path
from . import views

app_name = 'applicaton'
urlpatterns = [
    path('', views.index, name='index'),
]