from sqlmodel import SQLModel, Field
from typing import Optional

class Legend(SQLModel, table=True):
      id: Optional[int] = Field(default=None, primary_key=True)
      name: str
      category: str
      description: str
      date: str
      province: str
      canton: str
      district: str
      image_url: str
  