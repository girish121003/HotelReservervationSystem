from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns=[

    url(r'^$',views.index, name='index'),
    url(r'^signup/',views.signup,name='signup'),
    url(r'^user_login/$',views.user_login,name='login'),
    url(r'^logout/$', views.user_logout, name='Logout'),
    url(r'^search/',views.search_room,name='search')
]