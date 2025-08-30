from pydantic import BaseModel
import json

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}

address1 = Address(**address_dict)

patient_dict = {'name': 'nitish', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True) #default values will not be dumped

print(temp)
print(type(temp))

# Serialize the dictionary to a JSON string
user_json_string = json.dumps(temp, indent=2) # indent for pretty-printing

print(user_json_string)