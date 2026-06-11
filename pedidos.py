from pydantic import BaseModel, Field, field_validator

class Pedidos (BaseModel):
    cliente_id: int = Field (ge = 1)
    data_pedido: str
    status: str

    @field_validator ("status")
    def validacao_status (cls, status):
        
        status = status.title().strip()

        if status not in ['Entregue', 'Enviado', 'Processando']:
            raise ValueError('Status do pedido inválido.')

        return status