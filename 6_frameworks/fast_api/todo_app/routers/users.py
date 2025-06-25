from fastapi import APIRouter, Depends, HTTPException, Path
from models import Users
from database import SessionLocal
from typing import Annotated
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_curent_user

router = APIRouter(
    prefix="/user",
    tags=['user']
)

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def get_db():
    db = SessionLocal() # open connection
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_curent_user)]

@router.get("/", status_code=status.HTTP_200_OK)
def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    # probably not needed
    if user_model is None:
        raise HTTPException(status_code=404, detail='User not found')

    return user_model

@router.put("/change-password", status_code=status.HTTP_204_NO_CONTENT)
def change_password(user: user_dependency, db: db_dependency, old_password: str, new_password: str):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    user_local = db.query(Users).filter(Users.id == user.get('id')).first()
    if not user_local:
        return HTTPException(status_code=404, detail='User not found')
    if not bcrypt_context.verify(old_password, user_local.hashed_password):
        return HTTPException(status_code=401, detail='UInvalid credentials')
    
    user_local.hashed_password = bcrypt_context.hash(new_password)

    db.add(user_local)
    db.commit()