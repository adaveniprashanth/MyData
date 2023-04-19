from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body,Optional
from pydantic import BaseModel
app=FastAPI()



my_posts= [{'title':'my title0',"content":"my content0",'id':0},
           {'title':'my title1',"content":"my content1",'id':1},
           {'title':'my title2',"content":"my content2",'id':2},
           {'title':'my title3',"content":"my content3",'id':3},
           {'title':'my title4',"content":"my content4",'id':4}]
# path operation
@app.get("/") #here get means GET HTTP Method and "/" means path value
async def hello():
    return {"message":"welcome to my api"} #fastapi will convert the return value to json value


# POST path operation
@app.post("/postexample")
def create(payload: dict=Body(...)):
    print("payload",payload)
    return {"details":f"title is {payload['title']} and content is {payload['content']}"}

# validation of data from client
# creating the schema for validation
class Post(BaseModel):
    title:str  #this field is mandatory
    content:str #this field is mandatory
    published:bool = True  #giving default value if user not providing the field
    rating:Optional[int] = None #optional value


@app.post("/postexample1")
def create1(new_post:Post):
    print(new_post.dict()) #converting from object to dict
    return {"mandatory":f"title is {new_post.title} and content is {new_post.content}",
            "optional":f"published is {new_post.published} and rating is {new_post.rating}"}

# getting all posts from database/list
@app.get("/posts")
def get_posts():
    return {"data":my_posts}

# create a post
counter=5
@app.post('/createpost',status_code=status.HTTP_201_CREATED)#adding the default response code
def create_post(new_post:Post):
    new_post_dict = new_post.dict()
    global counter
    counter+=1
    new_post_dict['id']=counter
    my_posts.append(new_post_dict)
    return {"data":f"successfully saved {new_post_dict}"}

# get specific post details
@app.get("/posts/{id}")
def specific_post_details(id: int):#converting id from string type to int type
    if id >=0 and id  < len(my_posts):
        return {"data":my_posts[id]}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} was not found")

# deleting specific post
@app.delete('/posts/{id}',status_code=status.HTTP_204_NO_CONTENT)#adding the default response code
def delete_post(id:int):
    if id >= 0 and id < len(my_posts):
        my_posts.pop(id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with {id} was not found")

# update the specific post
@app.put("/posts/{id}")
def update_post(id:int,update_post:Post):
    if id < 0 and id >= len(my_posts):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"details about post {id} was not found")
    else:
        print(update_post.dict())
        my_posts[id]=update_post.dict()
        return {"message":"post updated"}
