from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Calculator(BaseModel):
    expression: str

@app.post("/calculate")
def calculate(request: Calculator):
    try:
        # simple calculation using eval (sirf basic operators)
        result = eval(request.expression)
        return {"expression": request.expression, "result": result}
    except Exception as e:
        return {"error": str(e)}
