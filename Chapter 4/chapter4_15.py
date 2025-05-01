from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()

async def pagination(q: str | None = None, skip: int = 0,
                     limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/cars/")
async def read_items(
    commons: Annotated[dict, Depends(pagination)]
):
    return commons
#     return {"q": commons["q"], "skip": commons["skip"], "limit": commons["limit"]}

@app.get("/users/")
async def read_users(
    commons:Annotated[dict, Depends(pagination)]
):
    return commons