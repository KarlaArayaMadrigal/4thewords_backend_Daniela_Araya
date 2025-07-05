from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
      # Implementar lógica de autenticación
      return {"access_token": "token", "token_type": "bearer"}
  