from django.urls import path

from . import views

# keeping all url which we use for this app  in this list
# the variable name must be urlpatterns only
# because we will export this list to main project urls.py file
urlpatterns = [
    # path( url_name, function_to handle, alias name for url_name)
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('homepage',views.homepage,name='homepage'),
    #whenever user goes to this link, it will call the function, then it will call the html page
    path('wordcounter',views.word_counter,name='wordcounter'),
    path('countwords',views.count_words,name='countwords'),
    path('modelsample',views.model_sample,name='modelsample'),
    path('modelsamples',views.model_samples,name='modelsamples'),
    path('dbmodelsample',views.db_model_sample,name='dbmodelsample'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # dynamic url routing
    # path('url_name/<datatype:variable_name>',function,alias)
    path('post/<str:name>', views.post, name='post'),
    path('dynamicroute', views.dynamic_route, name='dynamic'),
    path('blogs',views.blogs,name='blogs'),
    path('blogdetails/<str:id>', views.blog_details, name='blog_details'),
    path('weather', views.weather_request, name='weather'),
    path('chathome', views.chat_home, name='chathome'),
    path('room_name/<str:room_name>',views.chat_room,name='chatroom'),# here we can see the all the messages
    path('checkroom', views.check_room, name='checkroom'),

]