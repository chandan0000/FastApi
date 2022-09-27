from ast import Try
from typing import Optional, Union
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()
#  title str, content str, Bool punlished
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    try:

        conn = psycopg2.connect(
            host="localhost",
            database="fastapi",
            user="postgres",
            password="12345",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        # print("Database connection was succesfull!")
        break

    except Exception as error:
        print("Error while connecting to database")
        print(error)
        time.sleep(2)


@app.get("/")
def root():
    return {"message": "Welcome to apna api"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    data = cursor.fetchall()

    return {"data": data}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # cursor.execute(
    #     f"INSERT INTO posts (title, content, published) VALUES ({post.title, post.content, post.published})"
    # )

    cursor.execute(
        """
       INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *
        """,
        (post.title, post.content, post.published),
    )
    new_post = cursor.fetchone()
    conn.commit()
    conn.close()
    return {"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:  {id}  was not found",
        )

    return {"post_details": post}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # delete post
#     # find the index
#     index = find_index_post(id)
#     my_posts.pop(index)
#     print(index)
#     if index == 0:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     # find the index
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )
#     print(post)

#     my_posts[index] = post
#     return {"message": " post updated successfully", "data": my_posts[index]}
