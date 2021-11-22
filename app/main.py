from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth, post, user, vote

# Creates tables if they don't exist
# You don't need this if you use Alembic migrations
# models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth.router)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
