from fastapi import FastAPI,HTTPException,Depends,Response,APIRouter
from sqlalchemy.orm import Session
import models,oawth,pyd
from database import get_db

router=APIRouter()

@router.post("/votes")
def votes(vote:pyd.choice,db:Session=Depends(get_db),user_id=Depends(oawth.current_user)):
  print(user_id)
  table=db.query(models.likes).filter(vote.post==models.likes.post_id,user_id==models.likes.user_id)
  
  conflict=table.first()
  if(vote.choice==1):
    
    if conflict==None:
      row=models.likes(post_id=vote.post,user_id=user_id)
      db.add(row)
      db.commit()
      db.refresh(row)
      return{"success liked"}
    else:
      return{"alredy liked"}
  elif(vote.choice==0):
    if not conflict:
      return{"already unliked"}
    
    db.delete(conflict)
    db.commit()
    return Response(status_code=204)
    
  
      
  return {"invalid "}
    
  