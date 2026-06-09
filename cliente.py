from pydantic import BaseModel, Field, EmailStr, field_validator

class Cliente(BaseModel):
    nome: str = Field (min_length = 3)
    email: EmailStr
    cidade: str = Field (min_length = 3)
    
    @field_validator ("nome")
    def nome_deve_conter_espaco (cls, value, str) -> str:
        if ' ' not in value:
            raise ValueError ('O nome deve conter um espaço')
        return value
     