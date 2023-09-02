# https://pynative.com/python-class-method/
# https://pynative.com/python-class-method-vs-static-method-vs-instance-method/

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

    class child(parent1, parent2):
        def __init__(self, my_param):
            parent1.__init__(self, my_param=my_param)
            parent2.__init__(self, my_param=my_param)

    c=child(1,2)
    print(c.my_param)

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

if 1:
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