from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas, utils
from .databases import engine, get_db
from sqlalchemy.orm import Session
from .router import user, post


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Welcome to apna api"}
app.include_router(post.router)
app.include_router(user.router)
