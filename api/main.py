from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import math

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],  
)

class Calculator:
    def _init_(self):
        self.expression = ""

    def convert(self, expr: str):
        
        while "√" in expr:
            index = expr.index("√")
            n = ""
            i = index + 1
            while i < len(expr) and expr[i].isdigit():
                n += expr[i]
                i += 1
            expr = expr.replace(f"√{n}", f"math.sqrt({n})")

        
        while "²" in expr:
            index = expr.index("²")
            s = ""
            i = index - 1
            while i >= 0 and expr[i].isdigit():
                s = expr[i] + s
                i -= 1
            expr = expr.replace(f"{s}²", f"({s}**2)")

        return expr

    def calculate(self, expr: str):
        expr = self.convert(expr)

        
        allowed = {"math": math}

        try:
            result = eval(expr, allowed)
            return result
        except Exception as e:
            return f"Error: {e}"


calculator = Calculator()


@app.get("/calculate/")
def calculate(expression: str):
 

    result = calculator.calculate(expression)
    return {"expression": expression, "result": result}




if __name__ =="main_":
	uvicorn.run(app,host="127.0.0.1",port=8000)