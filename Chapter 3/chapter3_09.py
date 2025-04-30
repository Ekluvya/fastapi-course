from pydantic import BaseModel, Field
from typing import Literal

external_api_data = {
"user_id": 234,
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "age": 30,
    "account_type": "savings",
    "nickname": "Johnny",
}

class UserModelFields(BaseModel):
    id: int = Field(alias="user_id")
    username: str = Field(alias="name")
    email: str
    age: int | None = Field(None)
    account: Literal['savings', 'checking', 'credit'] | None = Field(None)
    nickname: str | None = Field(None)
    


user = UserModelFields.model_validate(external_api_data)
print(user)