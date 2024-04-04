"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include #include ta k import kora holo
admin.site.site_header = "Sudipto webtech Admin" #admin portal e change korar jonno
admin.site.site_title = "Sudipto webtech Portal" #admin portal e change korar jonno
admin.site.index_title = "Welcome to Sudipto webtech Portal" #admin portal e change korar jonno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), #j request asbe seta home er urls page e pathiya deba
]
