"""WhatsBio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from home.views import home
from contact.views import contact
from mycourse.views import mycourse
from searchApp.views import searchApp

app_name ='whatsbio'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mycourses/', mycourse, name='mycourses'),
    path('contact/', contact, name='contact'),
    path('allcourses/', include('allcourses.urls'), name='allcourses'),
    path('account/', include('account.urls'), name='account'),
    path('searchApp/', searchApp, name='searchApp'),
]

urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)