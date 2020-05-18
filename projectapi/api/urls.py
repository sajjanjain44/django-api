"""projectapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bryusers', views.UserView)

urlpatterns = [
    path('first_time_login/', views.first_time_login, name="first_time_login"),
    path('resend_otp/', views.resend_otp, name="resend_otp"),
    path('create_password/', views.create_password, name="create_password"),
    path('main_login/', views.main_login, name="main_login"),
    path('test/', views.test, name="test"),
    path('search_by_orderno/', views.search_by_orderno, name="search_by_orderno"),
    path('final_listing/', views.final_listing, name="final_listing"),
    path('search_by_name/', views.search_by_name, name="search_by_name"),
    path('change_password/', views.change_password, name="change_password"),
    path('verify_otp/', views.verify_otp, name="verify_otp"),
    path('forget_pass_clear_data_from_database/', views.forget_pass_clear_data_from_database, name="forget_pass_clear_data_from_database"),
    path('', include(router.urls)),
    path('user_logout/', views.user_logout, name="user_logout"),
]
