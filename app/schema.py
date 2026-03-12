from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class StandardCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    edition: Optional[float] = None
    organization: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = None


class StandardUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    edition: Optional[float] = None
    organization: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = None


class StandardOut(BaseModel):
    id: int
    name: str
    edition: Optional[float] = None
    organization: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
