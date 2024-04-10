from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return '¡Hola Leydi Linda!'


@app.get("/url")
async def root():
    return {"url":"https://leydifranco.com/python"}


## Iniciar el server: uvicorn main:app --reload
## Detener el server CTR+C
## Documentacion con Swagger http://127.0.0.1:8000/docs
## Documentacion con Redocly http://127.0.0.1:8000/redoc


