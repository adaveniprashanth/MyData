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
        value=0
        def __init__(self,thread_id,name,delay,counter):
            threading.Thread.__init__(self)
            self.id=thread_id
            self.name=name
            self.delay=delay
            self.counter=counter

        def run(self):
            # threadLock.acquire() #to lock resources
            while self.counter:
                mythread.value+=1
                print(self.name +" running"+" "+str(mythread.value))
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


    jessa = Student('Jessa', 20)
    jessa.show()

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

if 1:
    str1="prashanth abc"
    print(["".join(reversed(i)) for i in str1.split()])
    # print(" ".join(["".join(reversed(i)) for i in str1.split()]))

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