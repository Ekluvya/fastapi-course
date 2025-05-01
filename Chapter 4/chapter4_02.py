from fastapi import FastAPI

app = FastAPI()

@app.get("/car/{id}")
async def root(id):
    return {"car_id": id}

@app.get("/car/{id}")
async def root_int(id:int):
    return {"car_id": id}