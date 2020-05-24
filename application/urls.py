
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
    path('tasks/', views.tasks, name='tasks'),
    path('method/', views.method, name='method'),
    path('method/grade/<int:grade>/', views.method_grade, name='method_grade'),
    path('method/<int:rec_id>/text', views.recomendation_text, name='recomendation_text'),
]