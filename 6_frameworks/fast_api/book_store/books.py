from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_api():
    return {'Welcome': 'Mihai'}