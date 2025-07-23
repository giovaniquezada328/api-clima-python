from typing import Optional
from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime

def generate_id():
    return str(uuid4())

def generate_date():
    return str(datetime.now())


class Weather(BaseModel):
    id: Optional[str] = Field(default_factory=generate_id)
    city: str
    created_at: Optional[str] = Field(default_factory=generate_date)