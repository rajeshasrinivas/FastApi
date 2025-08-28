from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI()

data =  [{"id" : 1, "name" : "Ramesh", "weight": 70},
         {"id" : 2, "name" : "Anand", "weight": 85},
         {"id" : 3, "name" : "Dravid", "weight": 56},
         {"id" : 4, "name" : "Ullas", "weight": 92}]

# landing page
@app.get("/")
def fun():
    return { "message" : "landing page" }

#about page
@app.get("/about")
def fun():
    return { "message" : "about page" }

#path parameters
@app.get("/get_user/{uid}")
def fun(uid):
    for i in data:
        if int(uid) == i["id"]:
            return {"id" : i["id"], "name" : i["name"]}

    raise HTTPException(
            status_code=404,
            detail="Item not found")

#path parameters
@app.get("/improved_get_user/{uid}")
def fun(uid: int):
    for i in data:
        if uid == i["id"]:
            return {"id" : i["id"], "name" : i["name"]}
    raise HTTPException(
            status_code=404,
            detail="Item not found")

# using Path for validation and better docs
#path parameters
@app.get("/improved_get_user_1/{uid}")
def fun(uid: int = Path(..., description="Specify the id of the user", gt=0)):
    for i in data:
        if uid == i["id"]:
            return {"id" : i["id"], "name" : i["name"]}
    raise HTTPException(
            status_code=404,
            detail="Item not found")

#query parameters
@app.get("/sorted_view")
def fun(sort_key: str, sort_by: str="asc"):
    if sort_key not in ["id","name","weight"] or sort_by not in ["asc", "desc"]:
       raise HTTPException(
            status_code=404,
            detail="Veiw not possible please provide proper request")
    if sort_by == "asc":
        return list(sorted(data, key = lambda x: x[sort_key]))
    elif sort_by == "desc":
        return list(sorted(data, key = lambda x: x[sort_key], reverse=True))
       
# using Query for validation and better docs
#query parameters
@app.get("/improved_sorted_view")
def fun(sort_key: str = Query(..., description="view by id, name, weight"), sort_by: str= Query("asc", description="sort by asc or desc")):
    if sort_key not in ["id","name","weight"] or sort_by not in ["asc", "desc"]:
       raise HTTPException(
            status_code=404,
            detail="Veiw not possible please provide proper request")
    if sort_by == "asc":
        return list(sorted(data, key = lambda x: x[sort_key]))
    elif sort_by == "desc":
        return list(sorted(data, key = lambda x: x[sort_key], reverse=True))



##################### Note ##############################
# both path and query parameters can be used in same route
#########################################################
