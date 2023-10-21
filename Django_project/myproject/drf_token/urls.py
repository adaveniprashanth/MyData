from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token # to generate the authentication token
# to generate token from cmd prompt
# http post http://127.0.0.1:8000/drf_token/generatetoken username=admin1 password=prashanth

urlpatterns=[
    path('hello',views.Hello,name='hello'),
    path('helloview',views.HelloView.as_view(),name='helloview'),
    path('helloauth', views.HelloWithToken.as_view(), name='helloauth'),
    path('generatetoken',obtain_auth_token,name='generatetoken'),
]
