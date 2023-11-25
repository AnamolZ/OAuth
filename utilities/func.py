# app/func.py

from dataBase.dataBase import dataBase
from main import OAuth2PasswordBearer, CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def findPost(id):
    for i in dataBase:
        if i["postId"] == id:
            return i
        
def getHighlight(id, highlightId):
    for item in dataBase:
        if item["postId"] == id:
            for highlight in item["highlights"]:
                if highlight["highlight_number"] == highlightId:
                    return highlight
    return None

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)