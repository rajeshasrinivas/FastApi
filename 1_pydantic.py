from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

#Field to used for data Validation 
# optional values can be set by both Optional and Field 
# Annotated to Documentation
class patient(BaseModel):
    name: str = Field(default="new_patient")
    tests: Optional[Annotated[str, Field(max_length=10, title="name of tests", description="Tests performed")]] = "dummy_test"
    age: int = Field(ge=18, lt=80)
    interests: List[str] = Field(max_length=2)
    details: Dict[str,int]
    diseases: Optional[List[str]] = None
    email_id: EmailStr
    linkedin_url: AnyUrl = "https://www.linkedin.com/feed/"

data = {"name": "ram", "age": 30, "interests" : ["reading", "Jogging"], "details": {"age": 2, "val":10}, "email_id": "ram@gmail.com","age":74, "tests": "MRI" } 

patient_obj = patient(**data)

def veiw_data():
    print(patient_obj.name, patient_obj.age)

veiw_data()