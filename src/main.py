from fastapi import FastAPI
from settings import Settings
import uvicorn
import argparse
import dotenv
import os

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--env")
    args = parser.parse_args()
    if args.env and os.path.exists(args.env):
        dotenv.load_dotenv(args.env)
    
    APP_HOST = os.environ.get("APP_HOST")
    APP_PORT = int(os.environ.get("APP_PORT"))

    uvicorn.run(app, host=APP_HOST, port=APP_PORT) 