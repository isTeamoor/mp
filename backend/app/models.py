from pydantic import BaseModel, EmailStr
from typing import Optional, Annotated
from datetime import datetime
from fastapi import File, Form, UploadFile


class newCreatedAd(BaseModel):
    label: str
    textContent: str

class deletedAd(BaseModel):
    id: int








