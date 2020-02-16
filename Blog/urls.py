"""Realtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.urls import path
from Blog import views
from .views import (postlistview,postdetailview,postcreateview,postdeleteview,postupdateview)

urlpatterns = [

    path('About/', views.about,name='blog-about'),
    path('', views.postlistview.as_view(),name='blog-home'),
   path('post/<int:pk>/', views.postdetailview.as_view(),name='post-detail'),
    path('post/new/', views.postcreateview.as_view(),name='post-create'),
    path('post/<int:pk>/update/', views.postupdateview.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', views.postdeleteview.as_view(),name='post-delete'),
    path('user/<str:username>/', views.userpostlistview.as_view(),name='user-posts'),
]
