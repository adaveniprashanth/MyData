print("welcome to sql training")
import sqlite3
# For reference--> https://www.w3resource.com/sqlite/core-functions-replace.php for string methods
# for reference --> https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-datetime-function/
# For reference --> https://www.w3resource.com/sqlite/index.php
# For reference --> https://learnsql.com/cookbook/how-to-get-day-names-in-sqlite/
# For reference --> https://learnsql.com/cookbook/how-to-calculate-the-difference-between-two-dates-in-sqlite/
# python code for running the commands:
# sql='SELECT x FROM myTable WHERE x LIKE %s'
# args=[beginningOfString+'%']
# cursor.execute(sql,args)

# beginningOfString += '%'
# cursor.execute("SELECT x FROM myTable WHERE x LIKE ?", (beginningOfString,) )

#AUTOINCREMENT will work only when we use INTEGER PRIMARY KEY

# Connect to DB if exists or else create new database
database = sqlite3.connect('database2.db')
# <databasehandle>.create_function(<function name>,no.of arguments,operation)
database.create_function("strrev", 1, lambda s: s[::-1])
print("Opened database successfully")

#create a handle for database
cursor = database.cursor()

if 0: #REVERSE Method --> strrev(string)
    # <databasehandle>.create_function(<function name>,no.of arguments,operation)
    database.create_function("strrev", 1, lambda s: s[::-1])
    cursor.execute("SELECT strrev(first_name) AS 'short_name' FROM organisation;")
    for i in cursor:
        print(i)


def run_queries_from_file(filename):
    l = []
    with open(filename,'r') as file:
        for line in file:
            l.append(line.strip())
            # print(line)
    all_commans = "".join(l)
    cursor.executescript(all_commans)


if 1:
    if 1:#creating the tables
        run_queries_from_file('instagram_design_schema.sql')

    if 0:#printing the usernames(132) from the table
        data = cursor.execute('SELECT * FROM users;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing the photo urls(200) from the table
        data = cursor.execute('SELECT * FROM photos;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#joining the 2 tables
        data = cursor.execute('''SELECT image_url,username FROM photos INNER JOIN users ON photos.user_id=users.id;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#joining the 2 tables
        #IT WILL EXECUTE BUT WONT PRINT DATA
        cursor.executescript('''SELECT image_url,username FROM photos INNER JOIN users ON photos.user_id=users.id;''')
        # names = [i[0] for i in data.description]
        # print(names)
        for i in cursor:
            print(i)
    if 0:#printing all the comments(224)
        data = cursor.execute('SELECT * FROM comments;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing all the likes(100) list
        data = cursor.execute('SELECT * FROM likes;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#printing all the followers(200) list
        data = cursor.execute('SELECT * FROM follows;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#printing all the tag names(125)
        data = cursor.execute('SELECT * FROM tags;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#printing all the photo_tags(200)
        data = cursor.execute('SELECT * FROM photo_tags;')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

if 1:#exercise on instagram data
    if 0:#find the persons who have joined early
        data = cursor.execute("SELECT * FROM users ORDER BY created_at LIMIT 5;")
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#finding the day at which the most people are creating the account
        data = cursor.execute('''SELECT 
        strftime('%w',created_at) AS day,
        COUNT(*) AS total FROM users 
        GROUP BY day
        ORDER BY total DESC;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#finding the users who never posted any photo
        #joining users and photos so left part contains only the user who is not posted in the set
        data = cursor.execute('''
        SELECT username,image_url FROM users
         LEFT JOIN photos ON photos.user_id = users.id 
         WHERE photos.image_url is NULL;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#most liked photo in istagram
        data = cursor.execute('''
        SELECT photos.id,photos.image_url,COUNT(*) AS total FROM photos
        INNER JOIN likes ON photos.id = likes.photo_id
        GROUP BY photos.id ORDER BY total DESC LIMIT 1;
        ''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#most liked photo user in istagram
        data = cursor.execute('''
        SELECT users.username,photos.id,photos.image_url,COUNT(*) AS total FROM photos
        INNER JOIN likes ON photos.id = likes.photo_id
        INNER JOIN users ON photos.user_id = users.id
        GROUP BY photos.id ORDER BY total DESC LIMIT 5;
        ''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#average posts per user in istagram
        data = cursor.execute('''
        SELECT (SELECT COUNT(*) FROM photos) / (SELECT COUNT(*) FROM users) AS avg;''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)
    if 0:#most used 5 hashtags
        data = cursor.execute('''
        SELECT tags.tag_name, COUNT(*) AS total FROM tags
        INNER JOIN photo_tags ON tags.id = photo_tags.tag_id
        GROUP BY tags.tag_name ORDER BY total DESC LIMIT 5;
        ''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)

    if 0:#find the user who liked all photos
        data = cursor.execute('''
        SELECT users.username,COUNT(users.username) AS total_likes FROM users
        JOIN likes ON likes.user_id = users.id
        GROUP BY username
        HAVING total_likes = (SELECT COUNT(*) FROM photos);
        ''')
        names = [i[0] for i in data.description]
        print(names)
        for i in cursor:
            print(i)







#handler close
cursor.close()

#close database connection
database.close()
