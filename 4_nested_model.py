from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pincode:int

class Patient(BaseModel):
    name:str
    email:str
    age:int
    address: Address
address_dict={"city":"bangalore","state":"karnataka","pincode":560001}
address1=Address(**address_dict)
patient_dict={"name":"john","email":"aditya@hdfc.com","age":65,"address":address1}
patient1=Patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pincode)