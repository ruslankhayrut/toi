
from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('act/', views.act, name='act'),
    path('account/', views.account, name='account'),
    path('topic/<int:id>/', views.topic, name='topic'),
    path('info/<int:id>', views.info, name='info'),
    path('q/<int:id>', views.question, name='question'),

]