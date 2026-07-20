from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Welcome to FastAPI"}

'''
@app.get("/")

This is called a decorator.
It tells FastAPI:
"When someone sends a GET request to /, execute the function below."

home() - python func
return - FastAPI automatically converts the python dict into json
'''
