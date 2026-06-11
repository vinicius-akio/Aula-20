from pydantic import BaseModel, Field

class Marcas (BaseModel):
    nome: str = Field (min_length = 1)