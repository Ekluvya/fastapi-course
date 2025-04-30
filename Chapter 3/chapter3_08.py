from typing import Literal
from pydantic import BaseModel, Field

class UserModelFields(BaseModel):
    id: int = Field(...)
    username: str = Field(...)
    email: str = Field(...)
    account: Literal['savings', 'checking', 'credit'] | None = Field(None)
    nickname: str | None = Field(None)