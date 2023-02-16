from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import database as database, schemas as schemas, models.models as models, oauth2 as oauth2, utils.utils as utils


router = APIRouter(tags=['Authentication'])

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

  user = db.query(models.Usuario).filter(
    models.Usuario.login == user_credentials.username).first()

  if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Usuário inválido!")
  
  if not utils.verify(user_credentials.password, user.password):
    raise HTTPException(
          status_code=status.HTTP_403_FORBIDDEN, detail=f"Senha inválida!")

  access_token = oauth2.create_access_token(data={"user_id": user.id})

  return {"access_token": access_token, "token_type": "bearer"}