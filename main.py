from fastapi import FastAPI,HTTPException,Depends,Response
from fastapi import FastAPI,HTTPException,Depends,Response
from fastapi.params import Body
from random import randrange
import psycopg2
from sqlalchemy.orm import Session
from database import Base,engine,SessionLocal,get_db
import users,auth
import models
import pyd,oawth,likes

app = FastAPI()
models.Base.metadata.create_all(bind=engine)



try:
  conn=psycopg2.connect("dbname=new user=dusk")
  cur=conn.cursor()
  print("succesfully connected")
except Exception as error:
  print("eoror connectjng to db")



@app.get("/")
def root(db:Session=Depends(get_db),userid:int=Depends(oawth.current_user)):
  query=db.query(models.login).join(models.likes,models.login.id==models.likes.user_id,isouter=True)
  raw_sql = str(query.statement.compile(compile_kwargs={"literal_binds": True}))
  print(raw_sql)
  alldata =query.all()  
  
  return alldata

  
@app.post("/posts",response_model=pyd.post)
def post(input:pyd.pp,db: Session = Depends(get_db),userid:int=Depends(oawth.current_user)):
  print(userid)
  newpost=models.User(name=input.name,rating=input.rating,genre=input.genre,user_id=userid)
  db.add(newpost)
  db.commit()
  db.refresh(newpost)

  return newpost

@app.get("/posts/{id}")
def get_id(id:int,db: Session = Depends(get_db)):
  
  curid=db.query(models.User).filter(models.User.id==id).first();
  
  if curid==None:
    raise HTTPException(status_code=404,detail="not found in db")
  return{"succes":curid}
  
    
@app.delete("/posts/{id}",status_code=204)
def delpostid(id:int,db: Session = Depends(get_db)):
  curid=db.query(models.User).filter(models.User.id==id).first();
  
  if curid==None:
    raise HTTPException(status_code=404,detail="not found in db")
    
  db.delete(curid)
  db.commit()
  return Response(status_code=204)

@app.put("/posts/{id}")
def update_post(id:int,post:pyd.pp,db: Session = Depends(get_db)):
  posty=db.query(models.User).filter(models.User.id==id)
  print(posty)
  if posty.first()==None:
    return{"no post"}
  posty.update(post.dict(),synchronize_session=False)
  db.commit()
  return{"uodated pist"}





@app.get("/sqlal")
def test_func(db: Session = Depends(get_db)):
  mygames=db.query(models.User).all()
  return {"works":mygames}
  
#user login etc 
#db: Session = Depends(get_db)
#start

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(likes.router)

