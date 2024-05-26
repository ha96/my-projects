"""
URL configuration for todo_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup_view'),
    path('success/', views.success_view, name='success'),
    path('user_login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('puplic_post/', views.puplic_post, name='puplic_post'),
    path('admin/', admin.site.urls),
    path('pend_post/', views.pendingpost, name='pend_post'),
    path('showpost/<int:i>/', views.showpost),
    path('create_file/', views.create_file, name='create_file'),
    path('puplic_files/', views.puplic_files, name='puplic_files'),
    path('my_files/', views.my_files, name='my_files'),
    path('download_file/<int:file_id>/', views.download_file, name='download_file'),
    path('pendingfiles/', views.pendingfiles, name='pendingfiles'),
    path('showfile/<int:i>/', views.showfile),
    path('hidefile/<int:i>/', views.hidefile, name='hidefile'),
    path('hidepost/<int:i>/', views.hidepost, name='hidepost'),
    path('unusualactivity/', views.unusualactivity, name='unusualactivity'),
    path('scan_link/', views.scan_link, name='scan_link'),
]
