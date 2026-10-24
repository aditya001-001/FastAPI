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

temp=patient1.model_dump()
print(temp)
print(type(temp))

temp1=patient1.model_dump(include={'name'})
print(temp1)
print(type(temp1))

temp2=patient1.model_dump(exclude={'address':['state']})
print(temp2)
print(type(temp2))

temp3=patient1.model_dump(exclude_unset=True)
print(temp3)
print(type(temp3))
