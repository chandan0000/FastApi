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

# from typing import Optional, Union
# from fastapi import FastAPI, Response, status, HTTPException
# from pydantic import BaseModel
# from random import randrange

# app = FastAPI()
# #  title str, content str, Bool punlished
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     rating: Optional[int] = None


# my_posts = [
#     {
#         "title": "title of post 1",
#         "content": "content of post 1",
#         "id": 1,
#     },
#     {
#         "title": "favorite foods",
#         "content": "I Like Pizza",
#         "id": 2,
#     },
# ]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i
#         else:
#             return None


# @app.get("/")
# def root():
#     return {"message": "Welcome to apna api"}


# @app.get("/posts")
# def get_posts():
#     return {"data": my_posts}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     post_dict = post.dict()
#     post_dict["id"] = randrange(0, 1000000)
#     my_posts.append(post_dict)
#     return {"data": post_dict}


# @app.get("/posts/{id}")
# def get_post(id: int):
#     print(id)
#     post = find_post(id)
#     if not post:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id:  {id}  was not found",
#         )

#     return {"post_details": post}


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
