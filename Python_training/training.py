# https://pynative.com/python-class-method/
# https://pynative.com/python-class-method-vs-static-method-vs-instance-method/
# https://realpython.com/intro-to-python-threading/
import os
# os.system("echo $hello")

if 0:
    class parent1:
        def __init__(self,a):
            self.a=a

    class parent2:
        def __init__(self,b):
            self.b=b

    class child(parent1,parent2):
        def __init__(self,a,b,c):
            parent1.__init__(self,a)
            parent2.__init__(self,b)
            self.c=c

    ch=child(1,2,3)
    print(ch.a)
    print(ch.b)
    print(ch.c)
    print(child.mro())

if 0:#balanced paranthesis
    stack = []
    b = "(())))(())((())"
    for i in b:
        if i == "(":
            stack.append(")")
        elif i == ")" and ")" in stack:
            stack.remove(")")
    print(stack)

if 0:#syntactially correct paranthesis

    def isValid(sequence):
        while True:
            if '()' in sequence:
                sequence = sequence.replace('()', '')
            elif '{}' in sequence :
              sequence = sequence.replace ( '{}' , '' )
            elif '[]' in sequence :
              sequence = sequence.replace ( '[]' , '' )
            else:
                print(sequence)
                break
    isValid("))(())(")

if 0:# it will not work because super() will refer to the first parent class only
    class parent1:
        def __init__(self,a,**kw):
            self.a=a
    class parent2:
        def __init__(self,b,**kw):
            self.b=b
    class child(parent1,parent2):
        def __init__(self,a,b,c):
            super().__init__(a=a,**kw)
            super().__init__(b=b,**kw)
            self.c=c

    c=child(1,2,3)
    print(c.a)
    print(c.b)
    print(child.mro())

if 0:
    class parent1:
        def __init__(self, my_param):
            self.my_param = my_param

    class parent2:
        def __init__(self, my_param):
            self.my_param = my_param * 2

    class child(parent2, parent1):
        def __init__(self, my_param):
            parent2.__init__(self, my_param=my_param)
            parent1.__init__(self, my_param=my_param)


    c=child(1)
    print(c.my_param)
    print(child.mro())

if 0:
    class parent1:
        def __init__(self, a):
            self.a = a

    class parent2:
        def __init__(self, b,c):
            self.b = b * 2
            self.c=c

    class child(parent1, parent2):
        def __init__(self, data1,data2,data3):
            parent1.__init__(self, a=data1)
            parent2.__init__(self, b=data2,c=data3)

    ch=child(1,2,3)
    print(ch.c)

if 0:
    import threading,time
    threadLock=threading.Lock()
    class mythread(threading.Thread):

        def __init__(self,thread_id,name,delay,counter):
            threading.Thread.__init__(self)
            self.id=thread_id
            self.name=name
            self.delay=delay
            self.counter=counter

        def run(self):
            print("id values is",self.id)
            # threadLock.acquire() #to lock resources
            while self.counter:
                print(self.name +" running"+" "+str(self.counter))
                time.sleep(self.delay)
                self.counter -= 1
            # threadLock.release() # to release locked resources
    t1=mythread(1,"thread1",5,5)
    t2 = mythread(2, "thread2", 10,5)

    t1.start()
    t2.start()
    print("Exiting main thread")

if 0:
    class Student:
        school_name = 'ABC School'

        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def change_school(cls, school_name):
            # class_name.class_variable
            cls.school_name = school_name

        # instance method
        def show(self):
            print(self.name, self.age, 'School:', Student.school_name)

        @staticmethod
        def isAdult(age):
            return age > 18


    jessa = Student('Jessa', 20)
    jessa.show()
    print(Student.isAdult(22))

    # change school_name
    Student.change_school('XYZ School')
    jessa.show()

if 0:
    import time
    class Student:
        # constructor
        def __init__(self, name):
            print('Inside Constructor')
            self.name = name
        def show(self):
            print('Hello, my name is', self.name)
        # destructor
        def __del__(self):
            print('Object destroyed')


    # create object
    s1 = Student('Emma')
    s2 = s1
    s1.show()

    # delete object reference s1
    del s1
    # add sleep and observe the output
    time.sleep(5)
    print('After sleep')
    s2.show()

if 0: #creating socket acts as client and receiving data from server.
    # it is a client
    import socket
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.connect(('data.pr4e.org', 80))
    cmd='GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode() #conveting from string type to utf-8 format
    my_socket.send(cmd)

    while True:
        data=my_socket.recv(512)#collecting 512 bytes of data
        if len(data) <1:
            break
        print(data.decode())

    my_socket.close()

if 0:#creating the server
    from socket import *
    def startserver():
        serversocket = socket(AF_INET,SOCK_STREAM)
        try:
            serversocket.bind(('localhost',9000))#creating thehost and port number and binding them to server
            serversocket.listen(5)#making the server to listen mode
            while 1:
                (clientsocket,address) = serversocket.accept()# accepting the request from client and holding other client requests
                rd=clientsocket.recv(5000).decode()#receive 5k bytes from clinet and decode them to make python understand
                pieces=rd.split("\n")
                if len(pieces) > 0: print(pieces[0])#printing headers data
                data ='HTTP/1.1 200 OK\r\n'
                data+='Content-Type: text/html; character=utf-8\r\n'
                data+='\r\n'
                data+='<html><body><h1>The First Page</h1></body></html>'
                clientsocket.sendall(data.encode())#sending data to client
                clientsocket.shutdown(SHUT_WR)#closing the connection with client
        except KeyboardInterrupt:
            print("server stopped")
        except Exception as e:
            print("error",e)
        serversocket.close()
    print("access sever from http://loclahost:9000")
    startserver()
# keep below code in other file and run from other terminal
if 0:#connetingto the above crated server
    import urllib.request
    fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
    for line in fhand:
        print(line.decode().strip())

if 0:
    str1="prashanth abc"
    print(["".join(reversed(i)) for i in str1.split()])
    print("".join(list(reversed(str1))))
    print(" ".join(["".join(reversed(i)) for i in str1.split()]))

if 0:
    # import re
    str1 = "w2e1e1j3x1t8cf"
    # print(re.findall("\d+",str1))
    output=""
    digit=""
    for i in str1:
        if i.isdigit():
            digit+=i
        else:
            if digit != "":
                output+=int(digit)*i
                digit=""
            else:
                output+=i
    print(output)

if 0:
    s= 'asd'
    print("".join(reversed(s)))
    # print(dir(s))
    s= 'asd dfgs fdh'
    print(["".join(reversed(i)) for i in s.split()])

if 0:
    if 1:
        import urllib.request
        request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/')
        print(request_url.read())
    if 1:
        import urllib2
        req = urllib2.Request('http://www.example.com/')
        req.add_header('Referer', 'http://www.python.org/')
        resp = urllib2.urlopen(req)
        content = resp.read()
    if 1:
        import urllib.request
        url = "https://docs.python.org/3.4/howto/urllib2.html"
        hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }

        req = urllib.request.Request(url, headers=hdr)
        response = urllib.request.urlopen(req)
        response.read()

if 0:
    import requests,sqlite3

    database = sqlite3.connect('nishant_result.db')
    cursor =database.cursor()
    # Define the API endpoint
    url = "https://api.libring.com/v2/reporting/get"

    # Set the headers
    headers = {
        "Authorization": "Token RVyGynEAbqIfuidTkiYvKdEnn"
    }

    # Define the query parameters
    params = {
        "allow_mock": "true",
        "period": "custom_date",
        "start_date": "2023-01-01",  # Replace with your start date
        "end_date": "2023-01-02",    # Replace with your end date
        "group_by": "connection,app,platform,country",
        "lock_on_collection": "false"
    }

    # Make the GET request
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # The API response is stored in 'response.json()'
        api_data = response.json()
        # Do something with the data
        # print(api_data)
        # print(api_data['total_rows'])
        f=open('result.txt','w')
        for i in api_data['connections']:
            print(i)
            f.writelines(str(i)+"\n")
        f.close()
    else:
        print(f"Error: {response.status_code} - {response.text}")




if 0:
    import multiprocessing
    import time


    def long_running_function():
        # Your code here
        for i in range(10):
            time.sleep(1)
            print(f"Executing iteration {i + 1}")

    def main():
        # Set the maximum execution time (in seconds)
        max_execution_time = 5  # 5 seconds

        # Create a process to execute the function
        process = multiprocessing.Process(target=long_running_function)

        # Start the process
        process.start()

        # Wait for the process to complete or timeout
        process.join(timeout=max_execution_time)

        # If the process is still running, terminate it
        if process.is_alive():
            print("Execution exceeded 5 seconds. Stopping...")
            process.terminate()
            process.join()  # Ensure the process is terminated

        # Continue with the rest of your code
        print("Execution completed.")

    main()

if 0:
    import threading,time

    def long_running_function(i):
        # Your code here
        print("Executing...")
        time.sleep(i)


    # Set the maximum execution time (in seconds)
    max_execution_time = 10  # 5 minutes

    # Create a thread to execute the function
    execution_thread = threading.Thread(target=long_running_function,args=([30]))

    # Start the thread
    execution_thread.start()

    # Wait for the thread to complete or timeout
    execution_thread.join(timeout=max_execution_time)

    # If the thread is still running, stop it
    if execution_thread.is_alive():
        print("Execution exceeded 10 seconds. Stopping...")
        execution_thread.join()  # Ensure the thread is terminated

    # Continue with the rest of your code
    print("Execution completed.")

if 0:
    class pets:
        total_dogs=total_cats=total_fish=0
        def behaviour(self):
            print("my pet can fly,run or jump")

    class dog(pets):
        def __init__(self,name):
            self.name=name
            pets.total_dogs+=1
        def behaviour(self):
            print(f"{self.name} can run")

    d=dog("abc")
    print(pets.total_dogs)

#  SOLID principles

# Single responsibilty model ==> one class  takes only 1 responsibility
if 0:
    my_global_value=10
    class update_global: #always update the global value
        def __init__(self,value):
            global my_global_value
            my_global_value=value
            print("updated global value")
    class print_global: #always prints the global value
        def __init__(self):
            print("current global value is ",my_global_value)
    update_global(100)
    print_global()

# Open-closed principle #so in this one common values will be sned the to the parent
if 0:
    from abc import ABC, abstractmethod
    from math import pi

    class Shape(ABC):
        def __init__(self, shape_type):
            self.shape_type = shape_type
        @abstractmethod
        def calculate_area(self):
            pass
    class Circle(Shape):
        def __init__(self, radius):
            super().__init__("circle")
            self.radius = radius
        def calculate_area(self):
            return pi * self.radius ** 2
    class Rectangle(Shape):
        def __init__(self, width, height):
            super().__init__("rectangle")
            self.width = width
            self.height = height
        def calculate_area(self):
            return self.width * self.height
    class Square(Shape):
        def __init__(self, side):
            super().__init__("square")
            self.side = side
        def calculate_area(self):
            return self.side ** 2

    r =Rectangle(2,3)
    print(r.shape_type)
    print(r.calculate_area())

# Liscov principle
if 0:
    from abc import ABC,abstractmethod

    class Shape(ABC):
        def __init__(self,shape):
            self.shape_type=shape
        @abstractmethod
        def calculate_area(self):
            pass

    class Rectangle(Shape):
        def __init__(self,length,width):
            super().__init__("rectangle")
            self.length=length
            self.width=width

        def calculate_area(self):
            return self.length*self.width

    class Square(Shape):
        def __init__(self,side):
            super().__init__("square")
            self.side=side
        def calculate_area(self):
            return self.side**2

    r=Rectangle(2,3)
    s=Square(4)
    print(r.calculate_area())
    print(s.calculate_area())

# keeping same numbers adjescent in the order of 0,1,2
if 0:
    import random
    l=[random.choice([0,1,2]) for i in range(30) ]
    print(l)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                l[i],l[j]=l[j],l[i]
    print(l)

# generates the output of 2 nums which sums equal to target
if 0:
    import random
    l=[int(20*random.random()) for i in range(15)]
    # random.shuffle(l)
    print(l)
    left=0
    right=len(l)-1
    target=25
    res=[]
    while left < right:
        # print(l[left],l[right],l[left]+l[right])
        if l[left]+l[right] == target:
            res.append((l[left],l[right]))
            left+=1
            right-=1
        elif l[left] + l[right] < target:
            right -= 1
        else:
            left += 1
    print(res)
# generates the output of 3 nums which sums equal to target
if 0:
    from itertools import combinations
    import random
    l = [int(20 * random.random()) for i in range(15)]
    target=45
    res=[]
    for combination in combinations(l,3):
        # print(combination)
        if sum(combination) == target:
            res.append(combination)
    print(res)

# generate sub array which sum eqaul to target.
if 0:
    import random
    l = [int(20 * random.random()) for i in range(15)]
    target = 45
    print(l,target)
    res=[]
    for i in range(1,len(l)):
        for j in range(len(l)):
            # print(l[j:j+i])
            if j+i < len(l) and sum(l[j:j+i]) == target:
                res.append(tuple(l[j:j+i]))
    print(res)

# given 2 arrays in ascending order and merge them into single array in ascending order
if 0:
    import random
    nums1 = [int(20 * random.random()) for i in range(10)]
    nums2 = [int(20 * random.random()) for i in range(15)]
    nums1.sort()
    nums2.sort()
    l,m=len(nums1),len(nums2)
    print(nums1,nums2,l,m)
    left=right=0
    res=[]
    while left < l and right < m:
        if nums1[left]< nums2[right]:
            res.append(nums1[left])
            left+=1
        else:
            res.append(nums2[right])
            right+=1
    print(res)

# move 0's to end while maintaing  the order of other elements
if 0:
    l=[2,0,1,3,0,4,0,57,0,78,79,9,89,0,8,7,0,80,8,0,8,90,9,0,9,0,9,8]
    for i in range(len(l)):
        if  l[i] ==0:
            l.insert(len(l),l.pop(i))
    print(l)

if 0:
    print("31 LPA")
    print("LTIMINDTREE")
    basic = 67595
    bob = 126401
    basic_piece=16276
    bob_piece=12300+669
    print("basic"+39*" ",basic+basic_piece)
    print("bob" + 40 * " ", bob + bob_piece)
    a=base_salary=(basic+basic_piece+bob+bob_piece)*12
    print("base salary"+15*" ",a)
    b=variable=base_salary//10
    print("variable"+19*" ",b)
    c=TTC=a+b
    print("TTC"+23*" ",c)
    provident_piece=0
    provident=7511+provident_piece
    gratuaty_piece=1000
    gratuaty=3010+gratuaty_piece
    insurance_piece=2000+113-75

    insurance=12929+insurance_piece
    print("provident"+36*" ",provident)
    print("gratuaty"+37*" ",gratuaty)
    print("insurance"+19*" ",insurance)
    d=others=(provident+gratuaty)*12+insurance

    CTC=c+d
    print("other"+22*" ",d)
    print("CTC"+23*" ",CTC)
    # final_miss = 72
    # print(CTC-3100000-final_miss)

if 0:
    print("30 LPA")
    print("LTIMINDTREE")
    basic = 67595
    bob = 126401
    basic_piece=16276-3861
    bob_piece=12300+669-3715
    print("basic"+39*" ",basic+basic_piece)
    print("bob" + 40 * " ", bob + bob_piece)
    a=base_salary=(basic+basic_piece+bob+bob_piece)*12
    print("base salary"+15*" ",a)
    b=variable=base_salary//10
    print("variable"+19*" ",b)
    c=TTC=a+b
    print("TTC"+23*" ",c)
    provident_piece=0
    provident=7511+provident_piece
    gratuaty_piece=1000
    gratuaty=3010+gratuaty_piece
    insurance_piece=2000+116-75

    insurance=12929+insurance_piece
    print("provident"+36*" ",provident)
    print("gratuaty"+37*" ",gratuaty)
    print("insurance"+19*" ",insurance)
    d=others=(provident+gratuaty)*12+insurance

    CTC=c+d
    print("other"+22*" ",d)
    print("CTC"+23*" ",CTC)


if 0:
    print("30 LPA")
    print("innominds")
    a=basic=95000
    print("basic pay"+10*" ",basic,5*" ",basic*12)
    b=HRA=38000
    print("House RA"+11*" ",HRA,6*" ",HRA*12)
    c=meal_card=2200
    print("meal card"+11*" ",meal_card,7*" ",meal_card*12)
    d=LTA=18875
    print("Leave TA"+11*" ",LTA,6*" ",LTA*12)
    e=provident=1800
    print("provident"+11*" ",provident,7*" ",provident*12)
    f=gratuaty=3567
    print("gratuaty"+12*" ",gratuaty,7*" ",gratuaty*12)
    g=special_allowance=57558
    print("allowance"+10*" ",special_allowance,6*" ",special_allowance*12)
    h=variable1=12500
    print("variable1"+10*" ",variable1,6*" ",variable1*12)
    i=variable2=12500
    print("variable2"+10*" ", variable2,6*" ",variable2*12)
    total1=a+b+c+d+e+f+g+h+i
    print()
    print("total A" + 3 * " ", total1, 5 * " ", total1 * 12)
    j=telephone=3000
    print("telephone"+11*" ",telephone,7*" ",telephone*12)
    k=entertain=3000
    print("entertain"+11*" ",entertain,7*" ",entertain*12)
    l=books=1000+1000
    print("books"+15*" ",books,7*" ",books*12)
    total2=j+k+l

    print("total B"+5*" ",total2,7*" ",total2*12)
    CTC=total1+total2
    print("CTC"+7*" ",CTC,5*" ",CTC*12)

if 0:
    print("11 LPA")
    print("innominds")
    a=basic=33500
    print("basic pay"+10*" ",basic,5*" ",basic*12)
    b=HRA=10000
    print("House RA"+11*" ",HRA,6*" ",HRA*12)
    c=meal_card=2200
    print("meal card"+11*" ",meal_card,7*" ",meal_card*12)
    d=LTA=5864
    print("Leave TA"+11*" ",LTA,6*" ",LTA*12)
    e=provident=1800
    print("provident"+11*" ",provident,7*" ",provident*12)
    f=gratuaty=2572
    print("gratuaty"+12*" ",gratuaty,7*" ",gratuaty*12)
    g=special_allowance=12806
    print("allowance"+10*" ",special_allowance,6*" ",special_allowance*12)
    h=variable1=6742+720
    print("variable1"+10*" ",variable1,6*" ",variable1*12)
    i=variable2=6742+720
    print("variable2"+10*" ", variable2,6*" ",variable2*12)
    total1=a+b+c+d+e+f+g+h+i
    print()
    print("total A" + 3 * " ", total1, 5 * " ", total1 * 12)
    j=telephone=3000
    print("telephone"+11*" ",telephone,7*" ",telephone*12)
    k=entertain=3000
    print("entertain"+11*" ",entertain,7*" ",entertain*12)
    l=books=1000+1000
    print("books"+15*" ",books,7*" ",books*12)
    total2=j+k+l

    print("total B"+5*" ",total2,7*" ",total2*12)
    CTC=total1+total2
    print("CTC"+7*" ",CTC,5*" ",CTC*12)
    print(1100000-CTC*12)
    print(1100000/12)
# print(16000//12)
# print(1333/2)
# print((CTC*12-3100000)/12)
if 1:
    import subprocess
    import time
    import signal
    from streamlink import Streamlink

    # --- Configuration ---
    # Replace with the target website's live stream URL
    WEB_URL = 'https://stripchat.com/Hot_Misti_69'
    # Replace with your desired output file name (e.g., 'recording.mp4')
    OUTPUT_FILENAME = 'recording.mp4'
    # Desired stream quality (e.g., 'best', 'high', 'low', 'worst')
    STREAM_QUALITY = 'best'
    # Duration to record in seconds (for demonstration, set to a suitable time)
    RECORD_DURATION = 60  # Records for 60 seconds


    def record_stream(url, quality, output_file, duration):
        """
        Fetches stream URL using Streamlink and records using FFmpeg subprocess.
        """
        session = Streamlink()
        try:
            streams = session.streams(url)
            if not streams:
                print(f"No streams found for {url}")
                return

            # Get the URL for the desired quality stream
            stream_url = streams[quality].to_url()
            print(f"Found stream URL: {stream_url}")

            # Command to run FFmpeg as a subprocess
            ffmpeg_command = [
                'ffmpeg',
                '-i', stream_url,
                '-c', 'copy',  # Copy codecs to avoid re-encoding
                output_file
            ]

            print(f"Starting recording for {duration} seconds...")
            # Start FFmpeg process
            process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Wait for the specified duration
            try:
                time.sleep(duration)
            except KeyboardInterrupt:
                print("Recording interrupted by user...")
            finally:
                # Stop FFmpeg gracefully
                print("Stopping recording...")
                process.send_signal(signal.SIGINT)  # Use SIGINT to stop gracefully
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    print("FFmpeg process killed due to timeout.")

            print(f"Recording finished. File saved as {output_file}")

        except Exception as e:
            print(f"An error occurred: {e}")


    if __name__ == "__main__":
        record_stream(WEB_URL, STREAM_QUALITY, OUTPUT_FILENAME, RECORD_DURATION)

    # Replace with the actual URL of the YouTube live stream
    live_url = "https://stripchat.com/Hot_Misti_69"
    # record_youtube_live(live_url)
