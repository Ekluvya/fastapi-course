from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

user = User.model_validate(
    {
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "password123",
    }
)

print(user)