from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

## Inicia el server: uvicorn users:app --reload 

@app.get("/usersprueba")
async def usersprueba():
    return "Hola Usuarios de Leydi Franco"

class User(BaseModel): 
    id:int
    name: str
    surname:str
    url:str
    age:int

user_list = [User(id = 1, name= "Leydi", surname="Franco", url= "https://Leydi.com", age = 33), 
             User(id = 2, name= "Andres", surname="Cubillos", url= "https://andres.com", age = 23)]


@app.get("/userjson")
async def userjson():
    return [{"name": "Leydi", "surname":"Franco"}, 
            {"name":"Andres", "surname":"Cubillos"}]

@app.get("/users")
async def users(): 
    return user_list

@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try: 
        return list (users)[0]
    except:
        return {"Error":"No hay errores"} 
    

##Hay dos opciones de hacer el llamado, por Path y por Query
    ##path

@app.get ('/userquery/')
async def user(id:int):
    users = filter (lambda user: user.id == id, user_list)
    try:
        return list (user)[0]
    except:
        return {"error": 'No se encontraron errores'}
    

## Query 
    
    @app.get ("/user")
    async def user(id:int):
        return search_user(id)
    

