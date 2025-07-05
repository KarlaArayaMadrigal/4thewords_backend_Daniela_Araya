from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from models import Legend
from database import engine

router = APIRouter()

@router.post("/legends/")
def create_legend(legend: Legend):
      with Session(engine) as session:
          session.add(legend)
          session.commit()
          session.refresh(legend)
          return legend

@router.get("/legends/")
def read_legends():
      with Session(engine) as session:
          legends = session.exec(select(Legend)).all()
          return legends

@router.delete("/legends/{legend_id}")
def delete_legend(legend_id: int):
      with Session(engine) as session:
          legend = session.get(Legend, legend_id)
          if not legend:
              raise HTTPException(status_code=404, detail="Legend not found")
          session.delete(legend)
          session.commit()
          return {"message": "Legend deleted"}
  