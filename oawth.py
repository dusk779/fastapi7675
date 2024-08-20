import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime,timedelta

from fastapi import Depends,status,HTTPException
from fastapi.security import OAuth2PasswordBearer
from env import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES

awth2_scheme=OAuth2PasswordBearer(tokenUrl="auth")
def createtoken(data:dict):
  to_encode=data.copy()
  expire=datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})
  
  encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
  
  return encoded_jwt
  
def verifytoken(token:str,credentials_exception):
  try:
    pay=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    
    id:str=pay.get("user_id")
  
    if id is None:
      raise credentials_exception
      
    tokendata=id
    
    
  except InvalidTokenError:
    raise credentials_exception
    
  return tokendata
  
def current_user(token:str=Depends(awth2_scheme)):
  credentials_exception=HTTPException(status_code=401,detail="error verifying",headers={"WWW.Authenticate":"Bearer"})
  
  return verifytoken(token,credentials_exception)
    



