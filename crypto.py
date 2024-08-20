from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def Hash(password):
  return pwd_context.hash(password)
  
def verify(old_pass,hash_paas):
  return pwd_context.verify(old_pass,hash_paas)
