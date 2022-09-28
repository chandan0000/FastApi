# from typing import Optional, Union
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from random import randrange

# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     print(id)
#     post = find_post(id)
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message": f"post with id:  {id}  was not found"}
#     return {"post_details": post}

from ast import Try
# from typing import Optional, Union
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

# app = FastAPI()
# #  title str, content str, Bool punlished
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True


# while True:
#     try:

#         conn = psycopg2.connect(
#             host="localhost",
#             database="fastapi",
#             user="postgres",
#             password="12345",
#             cursor_factory=RealDictCursor,
#         )
#         cursor = conn.cursor()
#         # print("Database connection was succesfull!")
#         break

#     except Exception as error:
#         print("Error while connecting to database")
#         print(error)
#         time.sleep(2)


# @app.get("/")
# def root():
#     return {"message": "Welcome to apna api"}


# @app.get("/posts")
# def get_posts():
#     cursor.execute("""SELECT * FROM posts""")
#     data = cursor.fetchall()

#     return {"data": data}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # cursor.execute(
#     #     f"INSERT INTO posts (title, content, published) VALUES ({post.title, post.content, post.published})"
#     # )

#     cursor.execute(
#         """
#        INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *
#         """,
#         (post.title, post.content, post.published),
#     )
#     new_post = cursor.fetchone()
#     conn.commit()
#     conn.close()
#     return {"data": new_post}


# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
#     post = cursor.fetchone()

#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )

#     return {"post_details": post}


# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     cursor.execute("""DELETE FROM posts WHERE id = %s  returning*""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int, post: Post):
#     cursor.execute(
#         """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s returning*""",
#         (
#             post.title,
#             post.content,
#             post.published,
#             str(id),
#         ),
#     )
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )

#     return {"message": " post updated successfully", "data": updated_post}
