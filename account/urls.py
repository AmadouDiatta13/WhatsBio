from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.account, name='connectaccount'),
    path('signup/', views.signup, name='signup'),
    path('logoutaccount/', views.logoutaccount, name='logoutaccount'),
    path('loginaccount/', views.loginaccount, name='loginaccount'),
]