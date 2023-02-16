from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
import utils.utils as utils
from routers.auth import oauth2
import models.models as models
from database import get_db, engine
import schemas
from typing import List, Optional
from sqlalchemy.orm import Session
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

router = APIRouter(

)

@router.post("/reserva", status_code=status.HTTP_201_CREATED, response_model=schemas.Reserva)
def CreateReserva(reserva: schemas.CreateReserva, db: Session = Depends(get_db)):

  new_reserva = models.Reserva(**reserva.dict())
  db.add(new_reserva)
  db.commit()
  db.refresh(new_reserva)

  return new_reserva

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