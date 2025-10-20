from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional
import time
import re

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print(f"Request to {request.url.path} processed in {process_time:.4f} seconds")
    return response

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, regex="^[a-zA-Z0-9_]+$")
    email: str = Field(..., example="user@example.com")
    age: int = Field(..., gt=0, le=120)
    password: str = Field(..., min_length=8)

    @validator('email')
    def validate_email_domain(cls, v):
        if not re.match(r"[^@]+@[^@]+\.com$", v):
            raise ValueError('Email must have a .com domain')
        return v

@app.post("/users/", response_model=User)
async def create_user(user: User):
    return user

@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()}
    )
