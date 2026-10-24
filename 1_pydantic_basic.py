from pydantic import BaseModel
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    married:bool=False
    allergies:Optional[List[str]]=None
    contacts:Dict[str,str]
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contacts)
    print("inserted patient data successfully")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contacts)
    print("updated patient data successfully")

patient_info={"name":"john","age":30,"weight":72.3,"allergies":['dust','pollen'],"contacts":{"home":"1234567878","work":"8498283483"}}
patient=Patient(**patient_info)
update_patient_data(patient)