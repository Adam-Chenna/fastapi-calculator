from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import math

app = FastAPI()


class Expression(BaseModel):
    expression: str


@app.post("/calculate")
def calculate(data: Expression):
    expr = data.expression

    expr = expr.replace("^2", "**2")
    expr = expr.replace("sqrt", "math.sqrt")

    try:
        result = eval(
            expr,
            {"__builtins__": None, "math": math},
            {}
        )
        return {
            "expression": data.expression,
            "result": result
        }

    except:
        raise HTTPException(
            status_code=400,
            detail="Invalid expression"
        )
