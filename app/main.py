from random import randrange
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_posts = [{"title": "title of Post 1", "content": "content of post 1", "id": 1}, {"title": "title of Post 2", "content": "content of post 2", "id": 2}] # noqa

@app.get("/") # noqa
def first():
    return {"message": "We are Healthy"}

@app.get("/posts") # noqa
def get_posts():
    return{"data": my_posts}

def find_post(id): # noqa
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/posts/{id}") # noqa
def get_posts_by_id(id: int):
    post = find_post(id)
    return{"data": post}

@app.post("/create") # noqa
def create(payLoad: dict = Body(...)):
    return {"Created": f"title {payLoad['title']} content: {payLoad['content']}"} # noqa

# Post request using pydantic to do validation
class Post(BaseModel):  # noqa
    title: str
    content: str

@app.post("/posts") # noqa
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"Created" : post_dict} # noqa


@app.get("/hello/{name}") # noqa
def hello(name: str):
    return {"name": name}

@app.get("/min_of_two") # noqa
def minimum_of_two(num1: int, num2: int):
    if num1 < num2:
        return(num1)
    else:
        return(num2)

@app.get("/max_of_two") # noqa
def maximum_of_two(num1: int, num2: int):
    if num1 > num2:
        return(num1)
    else:
        return(num2)

@app.get("/profit_or_loss") # noqa
def profit_or_loss(CP: int, SP: int):
    if CP > SP:
        return("loss")
    else:
        return("profit")

@app.get("/is_vowel") # noqa
def isvowel(char: str):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        return("This is a vowel")
    else:
        return("This is not a vowel")

@app.get("/multiplication_tables") # noqa
def tables(num: int):
    tables = []
    for i in range(1, 11):
        list = (num, '*', i, '=', (num * i))
        tables.append(list)
    return tables
