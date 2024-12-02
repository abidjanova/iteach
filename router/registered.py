from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import database
from functions.registered import create_register, update_register, delete_register
from models.registered import Register
from router.login import get_current_active_user
from schemas.registered import CreateRegister
from schemas.user import CreateUser

register_router = APIRouter(
    prefix="/registered",
    tags=["Register"]
)

@register_router.get("/get_register")
def registerlarni_korish(db: Session = Depends(database)):
    return db.query(Register).all()


@register_router.post("/create_opinion")
def register_yaratish(form: CreateRegister, db: Session = Depends(database),
                       current_user: CreateUser = Depends(get_current_active_user)):
    create_register(form, db, current_user)
    raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.put("/update_register")
def register_tahrirlash(form: CreateRegister, register_id: int, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
     update_register(form, register_id, db, current_user)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")


@register_router.delete("/delete_register")
def registerni_ochirish(register_id: int, db: Session = Depends(database),
                    current_user: CreateUser = Depends(get_current_active_user)):
     delete_register(db, register_id, current_user)
     raise HTTPException(200, "Amaliyiot muvafaqiyatli amalga oshirildi")
