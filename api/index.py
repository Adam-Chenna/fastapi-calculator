from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Pydantic Model
class Expression(BaseModel):
    expression : str

@app.get("/")
def home():
    return {"message": "Calculator API is running 🚀"}

@app.post("/calculator")
def calculate(data : Expression):
    expr = data.expression.replace(" " , "")

    if "+" in expr :
        a,b = expr.split("+")
        result = float(a) + float(b)

    elif "-" in expr:
        a,b = expr.split("-")
        result = float(a) - float(b)
         
    elif "*" in expr:
        a,b = expr.split("*")
        result = float(a) * float(b)
    
    elif "/" in expr:
        a,b = expr.split("/")
        if b == 0:
            return{"Error" : "Cannot divide by zero"}
        
        else:
            result = float(a) / float(b)
    
    else:
        return {"Error" : "Invalid Choice"}
    
    return {
        "expression" : data.expression,
        "result": result
    }




