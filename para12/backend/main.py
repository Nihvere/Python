from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="API Менеджера задач")

# Ядро
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель данных
class TaskCreate(BaseModel):
    title: str


# Хранилище
tasks = [
    {"id": 1, "title": "Python", "completed": False},
    {"id": 2, "title": "Java", "completed": False},
]


# Энд поинт API
@app.get("/")
def home():
    return {"message": "FastAPI работает!"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "task deleted"}
    raise HTTPException(
        status_code=404,
        detail="Task not found",
    )


@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks", status_code=201)
def create_task(data: TaskCreate):
    new_task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": data.title,
        "completed": False,
    }
    tasks.append(new_task)
    return new_task



@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")



@app.patch("/tasks/{task.id}/toggle")
def toggle_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            return task
    raise HTTPException(status_code=404, detail="Task not found")



@app.get("/tasks/{task_id}/id")
def change_task_id(task_id: int, new_id = int):
    if any(task["id"] == new_id for task in tasks):
        raise HTTPException(
            status_code=400,
            detail="Task with this new_id already exists",
        )
    for task in tasks:
        if task["id"] == task_id:
            task["id"] = new_id
            return task
    raise HTTPException(
        status_code=404,
        detail="Task not found",
    )

@app.patch("/tasks/{task_id}/title")
def change_title(task_id: int, new_title: str):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            return task
    raise HTTPException(status_code=404, detail="Task not found")