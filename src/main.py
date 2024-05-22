from fastapi import FastAPI
from settings import Settings
import uvicorn

settings = Settings()
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    APP_HOST = settings.host
    APP_PORT = settings.port
    
    uvicorn.run(app, host=APP_HOST, port=APP_PORT) 