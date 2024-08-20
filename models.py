from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    rating = Column(Integer)
    genre= Column(String)
    created_at= Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
class login(Base):
  
  __tablename__="users"
  
  id = Column(Integer, primary_key=True)
  email=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  created_at= Column(TIMESTAMP, server_default=text('now()'))

class likes(Base):
  __tablename__="likes"
  
  post_id=Column(Integer,ForeignKey("games.id",ondelete="CASCADE"),primary_key=True)
  user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)