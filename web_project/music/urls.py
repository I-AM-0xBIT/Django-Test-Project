from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #music/20/
    path('<album_id>/',views.detail, name = 'detail'),
]