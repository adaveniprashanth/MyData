from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def Hello(request):
    context={'messgae':'hello world'}
    return Response(context)

class HelloView(APIView):
    def get(self,request):
        context={'message':'helloworld using helloview'}
        return Response(context)

class HelloWithToken(APIView):
    permission_classes = (IsAuthenticated,) # adding the permission checks
    def get(self,request):
        context={'message':'hello is coming after authentication'}
        return Response(context)
