from pydantic import BaseModel


class SubsSchema(BaseModel):
    id: int
    name: str
    price: float
    period: int
    
    class Config:
        from_attribute = True