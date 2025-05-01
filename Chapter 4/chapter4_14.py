from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

class InsertCar(BaseModel):
    brand: str
    model: str
    year: int

@app.post("/cars")
async def new_car(car: InsertCar):
    if car.year > 2023:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail="Year must be less than 2023"
        )
    return {"message": car}