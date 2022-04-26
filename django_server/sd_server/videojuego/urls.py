from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

urlpatterns = [
    path('',                    views.index,                name='index'),
    path('unityLogin',          views.unityLogin,           name='unityLogin'),
    path('main',                views.main,                 name='main'),
    path('unityLevelstats',     views.unityLevelstats,      name='unityLevelstats'),
    path('topScore',            views.topScore,             name='topScore'),
    path('login',               views.login,                name='login'),
    path('user_info',           views.user_info,            name='user_info'),
    path('stats',               views.stats,                name='stats'),
    path('priv',                views.priv,                 name='priv'),
    path('websiteRegister',     views.websiteRegister,      name='websiteRegister'),
    path('loginRegister',       views.loginRegister,        name='loginRegister'),
    path('giveMeUserData',      views.giveMeUserData,       name='giveMeUserData'),
    path('updateUserDataNow',   views.updateUserDataNow,    name='updateUserDataNow'),
    path('takeThisPhoto',       views.takeThisPhoto,        name='takeThisPhoto'),
    path('admin_panel',         views.admin_panel,          name='admin_panel'),
    path('users_data',          views.users_data,           name='users_data'),
    path('safe_admin_changes',  views.save_admin_changes,   name='safe_admin_changes'),
    path('delete_user',         views.delete_user,          name='delete_user'),
    path('to_admin_panel',      views.to_admin_panel,       name='to_admin_panel'),
    path('get_gaming_info',     views.get_gaming_info,      name='get_gaming_info'),
    # path('loginA', views.loginA, name='loginA')
    path('unityGamesession',    views.unityGamesession, name='unityGamesession'),
    path('unityCurrentlevel',   views.unityCurrentlevel,name='unityCurrentlevel')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

    #path('main', views.main, name='main'),
    #path('grafica', views.grafica, name='grafica'),
    #path('agr', views.agr, name='agr'),