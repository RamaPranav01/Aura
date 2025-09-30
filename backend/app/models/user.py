from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[UUID] = Field(default_new=uuid4, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    full_name: Optional[str] = None
    department: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)