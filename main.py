import uvicorn

if __name__ == "__main__":
    uvicorn.run("FastAPI.main:app", reload=True)