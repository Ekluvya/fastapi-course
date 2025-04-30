from pydantic import BaseModel, EmailStr, ValidationError, model_validator 
from typing import Any, Self

class UserModelV(BaseModel):
    id: int
    username: str
    email: EmailStr
    password1: str
    password2: str

    @model_validator(mode="after")
    def check_passwords_match(self) -> Self:
        pw1 = self.password1
        pw2 = self.password2

        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError("Passwords do not match")
        return self
    
    @model_validator(mode="before")
    @classmethod
    def check_private_data(cls, data: Any) -> Any:
        if isinstance(data, dict):
            assert(
                'private_data' not in data
            ), "Private data should not be included in the model"
        return data
    
usr_data = {
    "id": 1,
    "username": "john_doe",
    "email": "email@gmail.com",
    "password1": "password123",
    "password2": "password123",
    
}

try:
    user = UserModelV.model_validate(usr_data)
    print(user)
except ValidationError as e:
    print(e)