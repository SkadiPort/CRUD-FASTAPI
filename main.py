from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
my_app = FastAPI()

tasks = [
    {
    "id":1,
    "title":"Алгебра",
    "description":"195(1,2,3), 200(3,5)",
    "completed":False  
    },
    {
    "id":2,
    "title":"Геометрия",
    "description":"2015(1,2,3), 187(3,5)",
    "completed":True   
    }
]

    
       

@my_app.get('/',tags=["Задачи📚"],summary="Главная страница")
def home_route():
    return {
        "message":"Добро пожаловать в To-Do List Api!"
    }

@my_app.get("/todos/",tags=["Задачи📚"],summary="Получить все задачи")
def get_all_tasks():
    if tasks == []:
        return {
            "message":"Задач нет,добавьте их!"
        }
    else:
        return tasks

@my_app.get("/todos/{todo_id}",tags=["Задачи📚"],summary="Получить конкретную задачу")
def get_task(todo_id: int):
    for task in tasks:
        if task["id"] == todo_id:
            return task  
    raise HTTPException(status_code=404,detail="Задача не найдена")

class New_Task(BaseModel):
    title:str
    completed:bool
    description:str


@my_app.post("/todos",tags=["Задачи📚"],summary="Новая задача")
def create_task(new_task:New_Task):
    tasks.append({
        "id":len(tasks) + 1,
        "title":new_task.title,
        "completed":new_task.completed,
        "description":new_task.description
    })
    return {
        "message":"Задача успешно добавлена"
    }

@my_app.delete("/todos/{todo_id}",tags=["Задачи📚"],summary="Удалить задачу")
def delete_task(todo_id:int):
    for index, task in  enumerate(tasks):
        if task["id"] == todo_id:
            deleted_task = tasks.pop(index)
            return {
                "message":"Задача Удалена!"}
    raise HTTPException(status_code=404,detail="Задача не найдена для удаления")