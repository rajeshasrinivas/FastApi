from fastapi import FastAPI, HTTPException, Path, Query
import json

app = FastAPI()

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


# landing page
@app.get("/")
def fun():
    return { "message" : "landing page" }

#about page
@app.get("/about")
def fun():
    return { "message" : "about page" }


#path parameters
@app.get("/get_user/{pid}")
def get_patient_details(pid):
    data = load_data()
    if pid in data:
        return data[pid]

    raise HTTPException(
            status_code=404,
            detail="Item not found")

# using Path for validation and better docs
#path parameters
@app.get("/improved_get_user/{pid}")
def fun(pid: str = Path(..., description="Specify the pid of the user")):
    data = load_data()
    if pid in data:
        return data[pid]

    raise HTTPException(
            status_code=404,
            detail="Item not found")


#query parameters
@app.get("/sorted_view")
def sorted_data(sort_key: str, sort_by: str="asc"):
    data = load_data()
   
    if sort_key not in ["id","name","weight"] or sort_by not in ["asc", "desc"]:
       raise HTTPException(
            status_code=404,
            detail="Veiw not possible please provide proper request")
    if sort_by == "asc":
        return dict(sorted(data.items(), key=lambda item: item[1][sort_key]))
    elif sort_by == "desc":
        return dict(sorted(data.items(), key=lambda item: item[1][sort_key], reverse = True))

    
# using Query for validation and better docs
#query parameters
@app.get("/improved_sorted_view")
def fun(sort_key: str = Query(..., description="view by id, name, weight", ), sort_by: str= Query("asc", description="sort by asc or desc")):
    data = load_data()
    if sort_key not in ["id","name","weight"] or sort_by not in ["asc", "desc"]:
       raise HTTPException(
            status_code=404,
            detail="Veiw not possible please provide proper request")
    if sort_by == "asc":
        return dict(sorted(data.items(), key=lambda item: item[1][sort_key]))
    elif sort_by == "desc":
        return dict(sorted(data.items(), key=lambda item: item[1][sort_key], reverse = True))



##################### Note ##############################
# both path and query parameters can be used in same route
#########################################################

