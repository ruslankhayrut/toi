
from django.urls import path
from . import views

app_name = 'application'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('act/', views.act, name='act'),
    path('account/', views.account, name='account'),
    path('topic/<int:topic_id>/info/<int:info_id>/', views.info, name='info'),
    path('topic/<int:topic_id>/q/<int:question_id>/', views.question, name='question'),
]