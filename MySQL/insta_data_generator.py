if 0:#generate random  photo urls
    print("generate random number")
    import string,random
    # initializing size of string
    N = 20
    f = open('photo_urls.txt', 'w')
    for i in range(200):
        res = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
        print("The generated random string : " + str(res))
        number = random.randint(1, 132)
        print("The generated random number : " + str(number))
        f.writelines(['(',"'"'http://'+res,"'",",",str(number),')',','])
        if i%4 == 0:
            f.write("\n")
    f.close()

if 0:#generate random comments
    import string,random
    # initializing size of string
    input_file = open('comments.txt','r')
    output_file = open("insta_comments.txt",'w')
    data = input_file.read()
    for c,i in enumerate(data.split("\n"),1):
        user_id = random.randint(1, 132)
        photo_id = random.randint(1, 200)

        output_file.writelines(['(',"'",i.strip().lower(),"'",",",str(user_id),",",str(photo_id),')',','])
        print(i)
        if c%4 == 0:
            output_file.write("\n")
    input_file.close()
    output_file.close()
if 0:#generating data for instagram likes
    import random
    for i in range(100):
        user_id = random.randint(1, 132)
        photo_id = random.randint(1, 200)
        print("("+str(user_id)+","+str(photo_id)+"),")

if 1:#random date generator
    import random
    import time
    def random_date(start, end, time_format,prop):
        stime = time.mktime(time.strptime(start, time_format))
        etime = time.mktime(time.strptime(end, time_format))
        ptime = stime + prop * (etime - stime)
        return time.strftime(time_format, time.localtime(ptime))

    start = "1/1/2008 1:30:22"
    end= "1/1/2009 4:50:34"
    time_format = '%m/%d/%Y %I:%M:%S'
    # print(random_date(start,end,time_format,random.random()))

if 0:#generate followers table
    import random
    f = open('followers.txt','w')
    for i in range(200):
        follower_id = random.randint(1,132)
        followee_id = random.randint(1, 132)
        if follower_id != followee_id:
            f.write("("+str(follower_id)+","+str(followee_id)+"),")
        if i%6 == 0:
            f.write("\n")
    f.close()
if 0:#creating the data for the tags table
    f = open('insta_tags.txt','r')
    l= f.readlines()
    m = []
    f.close()
    for i in l:
        if i not in m:
            m.append(i)
    f = open('insta_tags.txt','w')
    f.writelines(m)
    f.close()
if 1:#creating teh data for the photo_tags table
    import random
    f = open('photo_tags.txt','w')
    for i in range(200):
        photo_id = random.randint(1,200)
        tag_id = random.randint(1,125)
        f.write("("+str(photo_id)+","+str(tag_id)+"),")
        if i%6 ==0:
            f.write("\n")
    f.close()
