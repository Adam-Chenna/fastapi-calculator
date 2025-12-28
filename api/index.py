from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Expression(BaseModel):
    expression: str

@app.get("/")
def home():
    return {"message": "Calculator API is running 🚀"}

@app.post("/calculator")
def calculate(data: Expression):
    expr = data.expression.replace(" ", "")

    # Empty input check
    if not expr:
        raise HTTPException(status_code=400, detail="Expression cannot be empty")

    try:
        if "+" in expr:
            a, b = expr.split("+")
            result = float(a) + float(b)

        elif "-" in expr:
            a, b = expr.split("-")
            result = float(a) - float(b)

        elif "*" in expr:
            a, b = expr.split("*")
            result = float(a) * float(b)

        elif "/" in expr:
            a, b = expr.split("/")
            b = float(b)
            if b == 0:
                raise HTTPException(status_code=400, detail="Cannot divide by zero")
            result = float(a) / b

        else:
            raise HTTPException(status_code=400, detail="Invalid operator")

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid number format")

    return {
        "expression": data.expression,
        "result": result
    }





