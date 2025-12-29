from fastapi import FastAPI

app = FastAPI()

@app.get("/calculator")

def calc(a : float , b : float , op = str):
    if op == "+":
        return {
            "Result" : {a+b}
        }
    
    elif op == "-":
        return {
            "Result" : {a-b}
        }
    
    elif op == "*":
        return {
            "Result" : {a*b}
        }
    
    elif op == "/":
        return {
            "Result" : {a/b}
        }
    
    else:
        Result : {Result}
        Expression : {op}
        return {
            "Error" : "Invalid Operator"
        }