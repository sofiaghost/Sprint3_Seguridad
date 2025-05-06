from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('historias/', views.historia_list, name='historiaList'),
    path('historia/<int:historia_id>', views.single_historia, name='singleHistoria'),
    path('historiaCreate/', csrf_exempt(views.historia_create), name='historiaCreate')
]