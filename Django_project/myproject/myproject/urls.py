"""
URL configuration for myproject project.

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
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    # importing the urls that supports to particular app. ex: firstapp
    path('firstapp/',include(('firstapp.urls','firstapp'),namespace='firstapp')), #providing namespace to avoid conflicts  between apps urls
    path('chatapp/',include(('chatapp.urls','chatapp'),namespace='chatapp')),
    path('apis/v1/',include(('apis.urls','apis'),namespace='apis')),
    path('notes/',include(('notes.urls','notes'),namespace='notes')),
    path('drf_token/', include(('drf_token.urls', 'drf_token'), namespace='drf_token')),
]
