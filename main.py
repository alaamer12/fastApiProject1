from fastapi import FastAPI

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/item/special")
async def special_item():
    return {"item_id": "Foo"}

@app.get("/item/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.post("/blog")
async def blog(blog: Blog):
    print(f"the blog with title {blog.title}")
    return blog.dict()