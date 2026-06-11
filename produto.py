from pydantic import BaseModel, Field, field_validator

class Produto(BaseModel):
    nome_produto: str = Field (min_length = 1)
    preco: str 
    marca_id: int = Field (ge = 1)
    estoque: int = Field (ge = 0)

    @field_validator ("nome_produto")
    def validacao_nome (cls, nome) -> str:
        
        nome = nome.title().strip()

        return nome

    @field_validator ("preco")
    def validacao_preco (cls, valor) -> float:

        try:
            valor = valor.replace(',', '.')
            valor = float(valor)

            return valor
    
        except:
            raise ValueError('Valor do produto inválido')
        