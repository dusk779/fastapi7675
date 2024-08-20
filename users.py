from fastapi import FastAPI,HTTPException,Depends,Response,APIRouter
import pyd
from sqlalchemy.orm import Session
from database import Base,engine,SessionLocal,get_db
import models,crypto




router=APIRouter();
@router.post("/users",status_code=201,response_model=pyd.returnuser)
def create_user(userinfo:pyd.createuser,db: Session = Depends(get_db)):
  hashedpassword= crypto.Hash(userinfo.password)
  userinfo.password=hashedpassword
  login=models.login(**userinfo.dict())
  db.add(login)
  db.commit()
  db.refresh(login)
  
  return login



