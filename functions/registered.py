from models.registered import Register
from fastapi import HTTPException

def create_register(form, db, current_user):
    if current_user.role == "admin":
        new_course = Register(
            name=form.name,
            phone_num=form.phone_num
        )
        db.add(new_course)
        db.commit()


def update_register(form, register_id, db, current_user):
    if current_user.role == "admin":
        db.query(Register).filter(Register.id == register_id).update({
            Register.name: form.name,
            Register.phone_num: form.phone_num
        })
        db.commit()
    else:
        raise HTTPException(404, "Siz admin emasiz")


def delete_register(db, register_id, current_user):
    if current_user.role == "admin":
        db.query(Register).filter(Register.id == register_id).delete()
        db.commit()
