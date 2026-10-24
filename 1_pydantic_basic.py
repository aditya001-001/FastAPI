from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
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

    @field_validator('email')
    @classmethod
    def email_validater(cls,value):
        valid_domians=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domians:
            raise ValueError('not a valid domain')
        return value
    @field_validator('age',mode='after')
    @classmethod
    def age_validater(cls,value):
        if value<0:
            raise ValueError('age cannot be negative')
        return value

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





patient_info={"name":"john","email":"aditya@hdfc.com","link":"https://example.com","age":'30',"weight":72.3,"allergies":['dust','pollen'],"contacts":{"home":"1234567878","work":"8498283483"}}
patient=Patient(**patient_info)
update_patient_data(patient)