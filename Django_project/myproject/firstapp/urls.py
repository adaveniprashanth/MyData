from django.urls import path
from . import views

# keeping all url which we use for this app  in this list
# the variable name must be urlpatterns only
# because we will export this list to main project urls.py file
urlpatterns = [
    # whenever user goes to this link, it will call the function, then function calls the html page
    # path( url_name, function_to handle, alias name for url_name)
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('homepage',views.homepage,name='homepage'),
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
    path('blogdetails/<str:id>', views.blog_details, name='blogdetails'),
    path('weather', views.weather_request, name='weather'),

    # chat application without namespace
    # path('chathome', views.chat_home, name='chathome'),
    # path('chat/<str:room>',views.room,name='chat'), # it will go to chat room
    # path('checkview', views.checkview, name='checkview'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/',views.getMessages,name='getMessages'),

    # my chat application without namespace means in project, we should have only one app
    # path('loginchat', views.login_chat, name='loginchat'),
    # path('joinroom',views.join_room,name='joinroom'),
    # path('chatsend', views.chat_send, name='chatsend'),
    # path('getHistory/<str:room>/',views.getHistory,name='getHistory'),

    # my chat application with namespace
    path('loginchatnamespace', views.login_chat_namespace, name='loginchatnamespace'),
    path('joinroomnamespace',views.join_room_namespace,name='joinroomnamespace'),
    path('chatsendnamespace', views.chat_send_namespace, name='chatsendnamespace'),
    path('getHistorynamespace/<str:room_value>/',views.getHistory_namespace,name='getHistorynamespace'),

]