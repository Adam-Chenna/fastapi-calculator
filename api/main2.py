from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

task = []

class Task(BaseModel):
    Task : str
    Completed : bool = False

@app.post("/add_task")

def add_task(tasks : Task):
    task.append(tasks)
    return {
        "message" : "Task Added",  "Task" : task
    }

@app.get("/show_task")

def show_task():
    return task

@app.put("/update_task/{task_id}")

def update_task(task_id : int, tasks : Task):
    if task_id < len(task):
        task[task_id] = tasks
        return {
            "message" : "Task Updated" , "Task" : task
        }
    return {
        "error" : "Task Not Found"
    }
    

@app.delete("/delete_task/{task_id}")

def delete_task(task_id : int):
    if task_id < len(task):
        delete = task.pop[task_id]
        return {
            "message" : "Task Deleted" , "Task" : delete
        }
    return{
        "message" : "Task Not found"
    }


        

