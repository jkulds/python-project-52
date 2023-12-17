"""
URL configuration for task_manager project.

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
from django.contrib.auth.views import LogoutView
from django.urls import path, include

import task_manager.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_manager.views.index, name='index'),
    path('users/', task_manager.views.users, name='users'),
    path('users/create/', task_manager.views.register, name='register'),
    path('users/<int:pk>/edit/', task_manager.views.edit_user, name='edit_user'),
    path('users/<int:pk>/delete/', task_manager.views.delete_user, name='delete_user'),
    path('login/', task_manager.views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('labels/', task_manager.views.register, name='labels'),

    path('statuses/', include('task_manager.status.urls')),

    path('tasks/', include('task_manager.task.urls'))
]
