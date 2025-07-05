from fastapi import FastAPI
from database import create_db_and_tables
from routers import legends, auth

app = FastAPI()

create_db_and_tables()

app.include_router(legends.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Legends API"}
