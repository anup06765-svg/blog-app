from django.urls import path

from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('newpost/', views.newpost, name='newpost'),
    path('mypost/', views.mypost, name='mypost'),
    path('signout/', views.signout, name='signout')
]
