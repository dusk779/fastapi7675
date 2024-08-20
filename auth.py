from fastapi import FastAPI,HTTPException,Depends,Response,APIRouter
from sqlalchemy.orm import Session
from database import Base,engine,SessionLocal,get_db
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pyd,models,crypto,oawth
from typing import Annotated


router=APIRouter()

@router.post("/auth")
def auth(user_cred:Annotated[OAuth2PasswordRequestForm, Depends()],db: Session = Depends(get_db)):
  user=db.query(models.login).filter(models.login.email==user_cred.username).first()
  if not user:
    return {"invakid crediantials"}
    
  if not  crypto.verify(user_cred.password,user.password):
    return{"invalid "}
  
  token= oawth.createtoken(data={"user_id":user.id})
  return {"loged in":token}
  
  