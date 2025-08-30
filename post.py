from fastapi import FastAPI, HTTPException, Path, Query
import json
from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated
from fastapi.responses import JSONResponse


app = FastAPI()

class Patient(BaseModel):
    id: str
    name: Annotated[str, Field(..., description="Name of the patient")]
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> float:
        if self.bmi <= 20:
            return "Normal"
        else:
            return "obese"
        
class Patient_update(BaseModel):
    
    name: Annotated[Optional[str], Field(default=None, description="Name of the patient")]
    weight: float = None
    height: float = None

#p_details = {"id":"P001","name" : "Ramesh", "weight": "70","height":1.72}

#validated_obj = Patient(**p_details)

def load_data():
    with open('data_1.json', 'r') as file:
        data = json.load(file)
    return data

def dump_data(data):
    with open('data_1.json', 'w') as file:
       json.dump(data, file,indent=2 )
    

@app.post("/insert_patient/")
def insert_record(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(detail="ID already exsist",status_code=400)
    else:
        data[patient.id] = patient.model_dump(exclude="id")
        dump_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient record Created"})


@app.put("/edit_patient/{patient_id}")
def insert_record(patient_id: str, patient_details: Patient_update):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(detail="ID Doesn't exsist",status_code=404)
    else:
        existing_data = data[patient_id]
        new_data      = patient_details.model_dump(exclude_unset=True)
        for key, value in new_data.items():
            existing_data[key] = value

        existing_data["id"] = patient_id
        updated_data = Patient(**existing_data)

        data[patient_id]  =  updated_data.model_dump(exclude="id")
        
        dump_data(data)
        return JSONResponse(status_code=200, content={"message": "Patient record edited"})



@app.delete("/delete_patient/{patient_id}")
def insert_record(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(detail="ID Doesn't exsist",status_code=404)
    else:
        del data[patient_id]
        dump_data(data)
        return JSONResponse(status_code=204, content={"message": "Patient record delete"})