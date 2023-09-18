from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Create a Pydantic model to define the input data structure
class Numbers(BaseModel):
    num1: float
    num2: float

# Define a route to handle addition
@app.post("/add")
async def add_numbers(numbers: Numbers):
    num1 = numbers.num1
    num2 = numbers.num2
    result = num1 + num2, num1 - num2
    return {"result": result}
