from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{id}")
async def root():
    return {"User_id": id}

@app.get("/user/me")
async def root_me():
    return {"User_id": "me"}
