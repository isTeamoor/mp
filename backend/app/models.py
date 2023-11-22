from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class newCreatedAd(BaseModel):
    label: str
    textContent: str

class deletedAd(BaseModel):
    id: int



