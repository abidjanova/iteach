from fastapi import FastAPI
from router.user import users_router
from router.login import login_router
from router.course import course_router
from router.opinion import opinion_router
from router.registered import register_router

app = FastAPI(docs_url="/")


app.include_router(users_router)
app.include_router(login_router)
app.include_router(course_router)
app.include_router(opinion_router)
app.include_router(register_router)
