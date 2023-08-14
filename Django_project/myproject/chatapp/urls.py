from django.urls import path
from . import views

urlpatterns=[
    # path( url_name, function_to handle, alias name for url_name)
    path('home', views.index, name='home'),
]