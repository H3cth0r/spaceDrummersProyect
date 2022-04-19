from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unityLogin', views.unityLogin, name='unityLogin'),
    path('main', views.main, name='main'),
    path('unityLevelstats', views.unityLevelstats, name='unityLevelstats'),
    path('topScore', views.topScore, name='topScore'),
    #path('main', views.main, name='main'),
    #path('grafica', views.grafica, name='grafica'),
    path('log_reg', views.log_reg, name='log_reg'),
    path('user_info', views.user_info, name='user_info'),
    path('stats', views.stats, name='stats'),
    #path('agr', views.agr, name='agr'),
    path('priv', views.priv, name='priv'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

