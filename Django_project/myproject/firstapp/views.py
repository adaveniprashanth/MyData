from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth # here User is like Usr table in database
from django.contrib import messages
from .models import feature,design,Post,Room  # importing the models from models.py file
import json
import urllib.request
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello world <h1>')

def home(request):
    name="guest"
    #here we have to inform to django to look into templates folder by updating the DIRS list
    # in the settings.py file in main project TEMPLATES list
    return render(request,'home.html',{'name':name})

def homepage(request):
    #passing dynamic data  as context
    context={'name':'raj','age':31}
    return render(request,'homepage.html',context)

def word_counter(request):
    return render(request,'word_counter.html')

def count_words(request):
    # we are using post method while calling url for this method in html page
    sentence = request.POST['sentence']
    # print(sentence)
    total = len(sentence.split(" "))
    context={
        'data':sentence,
        'total':total
    }
    return render(request,'counter_result.html',context)

def model_sample(request):
    feature1=feature()
    feature1.id=0
    feature1.name="first feature"
    feature1.description="this is a sample description"
    return render(request,'model_sample.html',{'feature':feature1})

def model_samples(request):
    feature1=feature()
    feature1.id=0
    feature1.name="first feature"
    feature1.description="this is a sample description"

    feature2 = feature()
    feature2.id = 1
    feature2.name = "second feature"
    feature2.description = "this is a sample description for other feature"
    features=[feature1,feature2]
    return render(request,'model_samples.html',{'features':features})

# for accessing the database, we need to change the database to sqlite3 in settings.py file in project
def db_model_sample(request):
    designs=design.objects.all() # collecting the data from database
    return render(request, 'db_model_sample.html', {'features': designs})

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist!') # showing the message
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'User already exist!') # showing the message
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()# saving user details in database user table
                messages.info(request, 'Success!')
                return redirect('login')
        else:
            messages.info(request, 'passwords not matched!')
            return redirect('register')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        # email=request.POST.get('email')
        # password = request.POST.get('password')
        print("user",username)
        print("email",email)
        print("pass",password)
        # user=auth.authenticate(email=email,password=password)# not working
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials!')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

# dynamic routing means the url link(i.e value in url) will change for each request
def post(request,name):
    # sample url is post/<name>
    return render(request,'post.html',{'name':name})

def dynamic_route(request):
    names = ["ram","raja","suresh","ajay"]
    return render(request,'dynamic_routing.html',{'names':names})

# database handling
def blogs(request):
    posts=Post.objects.all()
    return render(request,'blogs.html',{'posts':posts})

def blog_details(request,id):
    post=Post.objects.get(id=id)
    # print(post)
    return render(request,'blog_details.html',{'post':post})
# https://home.openweathermap.org/myservices -->Dummy@12
# api key ==> 97edf960d13ca46f1b75438d7f449e2a
# api request ==> http://api.openweathermap.org/data/2.5/weather?q=London&appid=97edf960d13ca46f1b75438d7f449e2a
def weather_request(request):
    if request.method=='POST':
        city=request.POST['city']
        res= urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=97edf960d13ca46f1b75438d7f449e2a').read()
        res=json.loads(res)
        print(res)
        data = {
            'city':res["name"],
            'coordinates':str(res["coord"]["lon"])+" "+str(res["coord"]["lat"]),
            'country_code':res["sys"]['country'],
            'temperature':res['main']['temp'],
            'pressure':res['main']['pressure'],
            'humidity': res['main']['humidity']
        }
    else:
        data={}
    return render(request,'weather_request.html',{'data':data})

def chat_home(request):
    return render(request,'chat_home.html')

def chat_room(request,room_name):

    return render(request,'chat_room.html') # this will help to enter into chat room

def check_room(request):
    if request.method =='POST':
        room_name=request.POST['room_name']
        user=request.POST['username']

        if Room.objects.filter(name=room_name).exists():
            return redirect('room_name/'+room_name+"/?username="+user)
        else:
            new_room=Room.objects.create(name=room_name) # creating the new room
            new_room.save()
            return redirect('room_name/' + room_name + "/?username=" + user)


