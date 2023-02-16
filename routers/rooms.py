from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter

from routers.auth import oauth2
import models.models as models
from database import get_db, engine
import schemas
from typing import Optional
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

router = APIRouter(

)

@router.post("/salas", status_code=status.HTTP_201_CREATED, response_model=schemas.Room)
def create_salas(room: schemas.CreateRooms, db: Session = Depends(get_db)):

  new_salas = models.Sala(**room.dict())
  db.add(new_salas)
  db.commit()
  db.refresh(new_salas)

  return new_salas


@router.get('/salas/{id}', response_model=schemas.Room)
def get_room(id: int, db: Session = Depends(get_db), room_id: int = Depends(oauth2.get_current_user)):
    room = db.query(models.Sala).filter(models.Sala.id == id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Sala com o id: {id}, não existe")

    return room


@router.delete("/salas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_room(id: int, db: Session = Depends(get_db), room_id: int = Depends(oauth2.get_current_user)):

    rooms_query = db.query(models.Sala).filter(models.Sala.id == id)

    room = rooms_query.first()

    if rooms_query == True:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Nenhuma sala encontrada com o: {id}")

    rooms_query.delete(synchronize_session=False)
    db.commit()

    return rooms_query

@router.get("/salas")
def get_rooms(db: Session = Depends(get_db),limit: int = 10, skip: int = 0, search: Optional[str] = "", ):
    rooms = db.query(models.Sala).all()
    return {"data": rooms}


@router.put("/salas/{id}")
def update_rooms(id: int, updated_post: schemas.CreateRooms, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):

    rooms_query = db.query(models.Sala).filter(models.Sala.id == id)

    users = rooms_query.first()

    if users == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    rooms_query.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    return rooms_query.first()
