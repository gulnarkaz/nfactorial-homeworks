from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

comments = []

class Comment(BaseModel):
    text: str
    category: str
    
@app.get("/")
def read_root():
    return {"message": "Welcome to Voxpop!"} 

@app.get("/about")
def read_about():
    return {"message": "VoxPop - это веб-платформа, предоставляющая возможность любому пользователю интернета оставлять комментарии на различные темы. Комментарии будут отображаться в общедоступной ленте."}

@app.post("/comment")
def add_comment(comment: Comment):
    comments.append(comment)
    return {"message": "Comment added successfully"}

@app.get("/comments/all", response_model=List[Comment])
def get_all_comments():
    return comments

@app.get("/comments/{category}", response_model=List[Comment])
def get_category_comments(category: str):
    return [comment for comment in comments if comment.category == category]

@app.get("/comments", response_model=List[Comment])
def get_comments(skip: int = 0, limit: int = 10):
    return comments[skip: skip + limit]
