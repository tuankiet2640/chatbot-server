from fastapi import FastAPI
from app.api import users

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)