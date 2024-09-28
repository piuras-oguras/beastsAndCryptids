from fastapi import FastAPI
from web import explorer,creature

app = FastAPI()

app.include_router(explorer.router)
app.include_router(creature.router)
@app.get("/")
def top():
    return "Góra Mahometa"

@app.get("/echo/{thing}")
def echo(thing):
    return f"Siema {thing}"
#http -b localhost:8000/echo/bestia
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True) #reload — jeśli będzie jakaś zmiana to uvicorn będzie działał
                                              # w sposób ciągły i restartował się jak będzie jakaś zmiana
