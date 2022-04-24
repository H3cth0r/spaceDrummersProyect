from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('unityLogin', views.unityLogin, name='unityLogin'),
    path('main', views.main, name='main'),
    path('unityLevelstats', views.unityLevelstats, name='unityLevelstats'),
    path('topScore', views.topScore, name='topScore'),
    path('login', views.login, name='login'),
    path('user_info', views.user_info, name='user_info'),
    path('stats', views.stats, name='stats'),
    path('priv', views.priv, name='priv'),
    path('websiteRegister',     views.websiteRegister,  name='websiteRegister'),
    path('loginRegister',       views.loginRegister,    name='loginRegister'),
    # path('loginA', views.loginA, name='loginA')
    path('unityGamesession', views.unityGamesession, name='unityGamesession'),
    path('unityCurrentlevel', views.unityCurrentlevel, name='unityCurrentlevel')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

    #path('main', views.main, name='main'),
    #path('grafica', views.grafica, name='grafica'),
    #path('agr', views.agr, name='agr'),