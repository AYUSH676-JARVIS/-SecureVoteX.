from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ElectionCreate(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime


class ElectionUpdate(BaseModel):
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    is_active: bool
    is_completed: bool


class ElectionResponse(BaseModel):
    id: str
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    is_active: bool
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)