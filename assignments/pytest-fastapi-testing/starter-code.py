from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API")


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(TaskCreate):
    completed: bool


class Task(TaskUpdate):
    id: int


tasks = [Task(id=1, title="Read the API guide", completed=False)]
next_task_id = 2


def find_task_record(task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found",
    )


def create_task_record(task_data: TaskCreate) -> Task:
    global next_task_id
    task = Task(
        id=next_task_id,
        title=task_data.title,
        completed=False,
    )
    next_task_id += 1
    tasks.append(task)
    return task


def update_task_record(task_id: int, task_data: TaskUpdate) -> Task:
    task = find_task_record(task_id)
    task.title = task_data.title
    task.completed = task_data.completed
    return task


def delete_task_record(task_id: int) -> None:
    task = find_task_record(task_id)
    tasks.remove(task)


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    return find_task_record(task_id)


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate):
    return create_task_record(task_data)


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    return update_task_record(task_id, task_data)


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    delete_task_record(task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
