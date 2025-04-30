from datetime import datetime
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    username: str
    email: str
    dob: datetime

Pu = User(id=1, username="johndoe", email="johndoe@example.com", dob=datetime(1990, 1, 1))
print(Pu)

try:
    user =  User(
    id="one",
    username="freethrow",
    email="email@gmail.com",
    dob=datetime(1975, 5, 13),
)
except ValidationError as e:
    print(e.json())