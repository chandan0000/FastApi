from fastapi import  Response, status, HTTPException, Depends,APIRouter
from .. import models, schemas, utils
from ..databases import engine, get_db
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/users",
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(users: schemas.UserCreate, db: Session = Depends(get_db)):
    # hash the password -user.password
    hash_password = utils.hash(users.password)
    users.password = hash_password
    new_user = models.User(**users.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} was not found",
        )
    return user
