from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from ..databases import engine, get_db
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix="/posts",
)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post1]
)
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post1
)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    print(new_post.create_at)
    return new_post


@router.get("/{id}", response_model=schemas.Post1)
def get_post(
    id: int,
    db: Session = Depends(get_db),
):

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:  {id}  was not found",
        )

    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):

    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:  {id}  was not found",
        )
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post1)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post1 = post_query.first()
    if post1 == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:  {id}  was not found",
        )
    post_query.update(
        post.dict(),
        synchronize_session=False,
    )
    db.commit()

    return post_query.first()
