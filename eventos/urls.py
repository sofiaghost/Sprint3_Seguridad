from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('eventos/', views.evento_list, name= 'eventoList'),
    path('eventoCreate/', csrf_exempt(views.evento_create), name='eventoCreate'),
]

