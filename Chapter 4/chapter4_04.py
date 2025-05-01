from enum import Enum
from fastapi import FastAPI, Path

app = FastAPI()

class AccountType(str, Enum):
    FREE = "free"
    PRO = "pro"


@app.get("/account/{account_type}/{months}")
async def account(account_type: AccountType, 
                  months: int = Path(..., ge=3, le=12)):
    return {"message": "Account Created", 
            "account_type":account_type,
            "months": months}