from pydantic import BaseModel,model_validator,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    link:AnyUrl
    age:int
    weight:float = Field(gt=0,lt=500)
    married:bool=False
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contacts:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergencycontact(cls,model):
        if model.age>60 and 'emergency' not in model.contacts:
            raise ValueError('emergency contact is required for age>60')


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contacts)
    print("inserted patient data successfully")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.link)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)

    print("updated patient data successfully")





patient_info={"name":"john","email":"aditya@hdfc.com","link":"https://example.com","age":'65',"weight":72.3,"allergies":['dust','pollen'],"contacts":{"home":"1234567878","work":"8498283483","emergency":"8498283483"}}
patient=Patient(**patient_info)
update_patient_data(patient)

# py 2_model_validator.py
# D:\FastAPI\2_model_validator.py:14: PydanticDeprecatedSince212: Using `@model_validator` with mode='after' on a classmethod is deprecated. Instead, use an instance method. See the documentation at https://docs.pydantic.dev/2.13/concepts/validators/#model-after-validator. Deprecated in Pydantic V2.12 to be removed in V3.0.
#   @model_validator(mode='after')
# D:\FastAPI\2_model_validator.py:45: UserWarning: A custom validator is returning a value other than `self`.
# Returning anything other than `self` from a top level model validator isn't supported when validating via `__init__`.
# See the `model_validator` docs (https://docs.pydantic.dev/latest/concepts/validators/#model-validators)for more details.
#   patient=Patient(**patient_info)
# john
# aditya@hdfc.com
# https://example.com/
# 65
# 72.3
# False
# ['dust', 'pollen']
# {'home': '1234567878', 'work': '8498283483', 'emergency': '8498283483'}
# updated patient data successfully
# (myenv) PS D:\FastAPI> 