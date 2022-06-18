from datetime import datetime
from pydantic import BaseModel


class WoeIdModel(BaseModel):
    id: int
    name: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    
    class Config:
        allow_mutation = False
        table_name = 'woeid'
