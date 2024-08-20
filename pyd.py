from pydantic import BaseModel,EmailStr
from datetime import datetime

class pp(BaseModel):
  name:str
  rating:int
  genre:str

class post(BaseModel):
  name:str
  rating:int
  genre:str
  created_at:datetime
  user_id:int
  
class createuser(BaseModel):
  email:EmailStr
  password:str
  
class returnuser(BaseModel):
  id:int
  email:EmailStr
  
class auth(BaseModel):
  email:EmailStr
  password:str
  
class choice(BaseModel):
  post:int
  choice:int