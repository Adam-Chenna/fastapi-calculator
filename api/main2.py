from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
tasks = {}
task_id_counter = 1

# Pydantic models
class TaskCreate(BaseModel):
    title: str
    description: str = None

class TaskUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

# ---------------- CRUD ----------------

# 1️⃣ Create task
@app.post("/tasks/")
def create_task(task: TaskCreate):
    global task_id_counter
    task_id = task_id_counter
    tasks[task_id] = {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    task_id_counter += 1
    return tasks[task_id]

# 2️⃣ Get all tasks
@app.get("/tasks/")
def read_tasks():
    return list(tasks.values())

# 3️⃣ Get single task
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

# 4️⃣ Update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task.title is not None:
        tasks[task_id]["title"] = task.title
    if task.description is not None:
        tasks[task_id]["description"] = task.description
    if task.completed is not None:
        tasks[task_id]["completed"] = task.completed

    return tasks[task_id]

# 5️⃣ Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return {"detail": "Task deleted"}
