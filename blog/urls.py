"""blog URL Configuration

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
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home",views.homeblog),
    path("sing",views.sing,name='sing'),
    path("login",views.login1,name='login'),
    path("profile",views.profile),
    path("logout",views.logout1,name='logout'),
    path("about",views.about,name='about'),
    path("delete/<int:id>",views.delete1),
    path("edit/<int:id>",views.edit1,name='edit'),
    path("contact",views.contact),
]
