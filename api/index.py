from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ast
import operator

app = FastAPI()

class Expression(BaseModel):
    expression: str

# Allowed operators only
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

def evaluate_expression(expr: str):
    def _eval(node):
        if isinstance(node, ast.Constant):  # numbers
            return node.value

        elif isinstance(node, ast.BinOp):  # + - * /
            op_type = type(node.op)
            if op_type not in allowed_operators:
                raise ValueError("Invalid operator")

            return allowed_operators[op_type](
                _eval(node.left),
                _eval(node.right)
            )

        elif isinstance(node, ast.UnaryOp):  # negative numbers
            return allowed_operators[type(node.op)](
                _eval(node.operand)
            )

        else:
            raise ValueError("Invalid expression")

    tree = ast.parse(expr, mode="eval")
    return _eval(tree.body)

@app.get("/")
def home():
    return {"message": "Advanced Calculator API running 🚀"}

@app.post("/calculator")
def calculate(data: Expression):
    if not data.expression:
        raise HTTPException(status_code=400, detail="Expression cannot be empty")

    try:
        result = evaluate_expression(data.expression)
        return {
            "expression": data.expression,
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid mathematical expression")




