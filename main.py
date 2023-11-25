# app/main.py

from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from typing import List, Optional
from pydantic import BaseModel, EmailStr
import random

from model.models import PostModel, UpdateModelWithHighlight, UpdateModelWithoutHighlight
from dataBase.dataBase import dataBase
from utilities.func import findPost

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from security.oauth import TokenData, get_current_user

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return "Root Directory"

@app.post("/root/postCreation")
async def postCreation(dataBaseM: PostModel, current_user: TokenData = Depends(get_current_user)):
    dataBase.append(dataBaseM)
    return "Post Created"

@app.get("/root/postRetrieval")
async def postRetrieval(current_user: TokenData = Depends(get_current_user)):
    return {"Post Retrieval" : dataBase}

@app.get("/root/postRetrieval/{postId}")
async def postRetrieval(postId: int, current_user: TokenData = Depends(get_current_user)):
    postFetch = findPost(postId)
    return {"Post Fetch" : postFetch}

@app.put("/root/postUpdate/{postId}")
async def postUpdateWithoutHighlight(postId: int, dataBaseM: UpdateModelWithoutHighlight, current_user: TokenData = Depends(get_current_user)):
    postFetch = findPost(postId)
    if not postFetch:
        raise HTTPException(status_code=404, detail="Post Not Found")
    
    for i in ['title','content','tips']:
        if dataBaseM.dict()[i]:
            postFetch[i] = dataBaseM.dict()[i]

    return {"Post Update": postFetch}, 200

@app.put("/root/postUpdate/{postId}/{highlightId}")
async def postUpdateWithHighlight(postId: int, highlightId: int, dataBaseM: UpdateModelWithHighlight):
    
    postFetch = findPost(postId)
    validRangeMax = len(postFetch["highlights"])
    validRangeMin = 1
    highlightRange = range(validRangeMin, validRangeMax + 1)

    if postFetch:
        if highlightId in highlightRange:
            tempVar = postFetch["highlights"][highlightId - 1]
            tempVar.update(dataBaseM.highlights[0].dict(exclude_unset=True))
            return {"Post Update": postFetch}, 200
        else:
            raise HTTPException(status_code=404, detail="Highlight Not Found")
    else:
        raise HTTPException(status_code=404, detail="Post Not Found")
    
@app.delete("/root/postDelete/{postId}")
async def postDelete(postId: int, current_user: TokenData = Depends(get_current_user)):
    try:
        postFetch = findPost(postId)
        if not postFetch:
            raise HTTPException(status_code=404, detail="Post Not Found")
        
        dataBase.remove(postFetch)
        return {"Post Delete": "Done"}, 200
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
