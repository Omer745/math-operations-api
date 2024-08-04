from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

class NumberOperators(BaseModel):
    numbers: list[int]
    operation: str 

class NumberOperator2(BaseModel):
    source_num : int
    numbers: list[int]
    operation: str 

app = FastAPI()

def sumlist(numbers: list[int]):

    response = 0
    for number in numbers:
        response += number

    return response

def multiplylist(numbers: list[int]):

    response = 1
    for number in numbers:
        response *= number

    return response

def dividelist(sourc_num: int, numbers: list[int]):

    for number in numbers:
        sourc_num /= number
    
    return sourc_num

def subtractlist(sourc_num: int, numbers: list[int]):

    for number in numbers:
        sourc_num -= number    
    return sourc_num


@app.post("/sum-multiply")
def sum_multiply(Request: NumberOperators):
    if Request.operation == "sum":
        return {"result": sumlist(Request.numbers)}

    if Request.operation == "multiply":
        return {"result": multiplylist(Request.numbers)}    


@app.post("/divide-subtract")
def divide_multiply(Request: NumberOperator2):
    if Request.operation == "divide":
        return {"result": dividelist(Request.source_num,Request.numbers)}
    if Request.operation == "subtract":
        return {"result": subtractlist(Request.source_num,Request.numbers)}        
    return {"result": "Invalid operation"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
