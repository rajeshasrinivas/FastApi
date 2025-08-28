from fastapi import FastAPI

app = FastAPI()

# landing page
@app.get("/")
def fun():
 return { "message" : "Hello World!!!" }
 