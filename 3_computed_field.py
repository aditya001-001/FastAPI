from pydantic import BaseModel,model_validator,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional

class Patient(BaseModel):
    name:str
    email:EmailStr
    link:AnyUrl
    age:int
    weight:float = Field(gt=0,lt=500)#kg
    hieght:float = Field(gt=0,lt=4)#mtrs
    married:bool=False
    allergies:Optional[List[str]]=Field(default=None,max_length=5)
    contacts:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=self.weight/(self.hieght**2)
        return round(bmi,2)


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
    print("Bmi",patient.bmi)

    print("updated patient data successfully")





patient_info={"name":"john","email":"aditya@hdfc.com","link":"https://example.com","age":'65',"weight":72.3,"hieght":1.75,"allergies":['dust','pollen'],"contacts":{"home":"1234567878","work":"8498283483","emergency":"8498283483"}}
patient=Patient(**patient_info)
update_patient_data(patient)
