from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fun():
 return "{ "message" : "Hello World!!!" }"