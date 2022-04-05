from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unityLogin', views.unityLogin, name='unityLogin'),
    path('unityLevelstats', views.unityLevelstats, name='unityLevelstats'),
    #path('main', views.main, name='main'),
    path('grafica', views.grafica, name='grafica')
]

