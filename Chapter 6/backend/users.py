import json
import uuid
from fastapi import APIRouter, Depends, Body, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from authentication import AuthHandler
from models import UserBase, UserIn, UserOut, UsersList

router = APIRouter()
auth_handler = AuthHandler()

@router.post("/register",
             response_description="Resgister a new user",)
async def register(
    request: Request,
    newUser: UserIn = Body(...),
) -> UserBase:
    users = json.loads(open("users.json").read())["users"]
    newUser.password = auth_handler.get_password_hash(newUser.password)

    if any(user["username"] == newUser.username for user in users):
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    newUser = jsonable_encoder(newUser)
    newUser["id"] = str(uuid.uuid4())
    users.append(newUser)
    with open("users.json", "w") as f:
        json.dump({"users": users}, f, indent=4)
    return newUser

@router.post("/login",
                response_description="Login a user")
async def login(
    request: Request,
    loginUser: UserIn = Body(...),
) -> str:
    users = json.loads(open("users.json").read())["users"]
    user = next(
        (user for user in users if user["username"] == loginUser.username),
        None
    )
    if (user is None) or (not
                          auth_handler.verify_password(
                              loginUser.password,
                                user["password"]
                          )):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    token = auth_handler.encode_token(
        str(user["id"]),
        user["username"])
    response = JSONResponse(content={
        "token": token
    })
    return response

@router.get("/list", response_description="List all users")
async def list_users(
    request: Request,
    user_data=Depends(auth_handler.auth_wrapper)
):
    users = json.loads(open("users.json").read())["users"]
    return UsersList(users=users)