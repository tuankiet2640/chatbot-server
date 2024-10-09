from fastapi import FastAPI
from app.api import users,authentication, chat, rag
app = FastAPI()

app.include_router(users.router, prefix="/api/v1", tags = ["user management"])
app.include_router(authentication.router, prefix="/api/v1", tags=["authentication"])
app.include_router(chat.router, prefix="/api/v1", tags =["chat"])
app.include_router(rag.router, prefix="/api/v1/rag")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)