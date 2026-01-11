from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class Expression(BaseModel):
    expression : str


@app.post("/claculate")

def calculate(data : Expression):
    expr = data.expression

    expr = expr.replace("^2" ,"**2")
    expr = expr.replace("sqrt" , "math.sqrt")

    try :
        

    
