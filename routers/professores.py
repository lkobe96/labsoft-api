from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
import utils.utils as utils
from routers.auth import oauth2
import models.models as models
from database import get_db, engine
import schemas
from typing import List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.params import Body
from typing import List, Optional

models.Base.metadata.create_all(bind=engine)

router = APIRouter(

)

@router.get('/teacher/{id}', response_model=schemas.Professor)
def get_teacher(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    teacher = db.query(models.Professor).filter(models.Professor.id == id).first()
    if not teacher:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuário com o id: {id} não existe")

    return teacher


@router.post("/teacher", status_code=status.HTTP_201_CREATED, response_model=schemas.Professor)
def create_teacher(teacher: schemas.CreateProfessor, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

  new_teacher = models.Professor(**teacher.dict())
  db.add(new_teacher)
  db.commit()
  db.refresh(new_teacher)

  return new_teacher

@router.delete("/teacher", status_code=status.HTTP_204_NO_CONTENT)
def delete_teacher(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    teacher_query = db.query(models.Professor).filter(models.Professor.id == id)

    teacher = teacher_query.first()

    if teacher == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Usuário com o id: {id} não existe")
    
    if teacher.type_user != oauth2.get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="não autorizado  to perform requested action")

    teacher_query.delete(synchronize_session=False)
    db.commit()

    return teacher_query