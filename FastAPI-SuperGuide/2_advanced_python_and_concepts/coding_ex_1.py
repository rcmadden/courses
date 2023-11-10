"""
Your goal is to create a social media post model using pydantic. The model should have:
An author, which is a string
An optional co-author, which is a string
A date, which is a string
A title, which is a string
The content, which is a string
An ID, which is an integer
Likes, which is a list of strings

The post should also have a field for comments, 
which is a list of comment models. 
The model should have:
An author, which is a string
The comment, which is a string
Likes, which is an integer

Practice creating a social media post with whatever data you like, so long as it compiles.
"""
from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    author: str
    comment: str
    likes: int

class Post(BaseModel):
    author: str
    co_author: Optional[str] = None
    date: str
    title: str
    content: str
    id: int
    likes: List[str]
    comments: List[Comment]

comments = [
        Comment(author='Jenn', comment='Great post!', likes=3),
        Comment(author='Sam', comment='Super post!', likes=6)
        ]

new_post = Post(
    author='Russia',
    date='2021-01-01',
    title='First Post',
    content='hello world',
    id=1,
    likes=['Jenn', 'Sam'],
    comments=comments
    )
print(new_post.comments[0].author)
print(new_post)
# author='Russia' co_author=None date='2021-01-01' title='First Post' content='hello world' id=1 likes=['Jenn', 'Sam'] comments=[Comment(author='Jenn', comment='Great post!', likes=3), Comment(author='Sam', comment='Super post!', likes=6)]