from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.security import HTTPBasic, HTTPBasicCredentials

from db import Base, engine
from router.course import course_router
from router.opinion import opinion_router
from router.registered import register_router
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Oybekjon",
              docs_url=None)

app.mount("/images", StaticFiles(directory="images"), name="images")

Base.metadata.create_all(bind=engine)


app.include_router(course_router)
app.include_router(opinion_router)
app.include_router(register_router)

# security = HTTPBasic()
#
#
# def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
#     correct_username = "oybekjon"
#     correct_password = "oybekjon"
#     if credentials.username != correct_username or credentials.password != correct_password:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Noto'g'ri login yoki parol",
#             headers={"WWW-Authenticate": "Basic"},
#         )
#     return credentials.username
#
#
# @app.get("/docs", include_in_schema=False)
# def custom_swagger_ui_html(credentials: HTTPBasicCredentials = Depends(get_current_user)):
#     from fastapi.openapi.docs import get_swagger_ui_html
#     return get_swagger_ui_html(openapi_url=app.openapi_url, title="Iteach")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)