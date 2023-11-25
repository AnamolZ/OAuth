# app/func.py

from dataBase.dataBase import dataBase
from dataBase.credentialBase import db_users
from model.models import User

from main import OAuth2PasswordBearer, CryptContext

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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):
    if username in db_users:
        user_dict = db_users[username]
        return User(**user_dict)

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user