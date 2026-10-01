from fastapi import FastAPI
from uvicorn import run
from views.api import router as api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)
