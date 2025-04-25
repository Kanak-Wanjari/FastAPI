from pydantic import BaseModel, ConfigDict

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemOut(ItemCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)