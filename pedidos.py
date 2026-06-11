from pydantic import BaseModel, Field, field_validator
import datetime

class Pedidos (BaseModel):
    cliente_id: int = Field (ge = 1)
    data_pedido: str
    status: str

    @field_validator ("data_pedido")
    def validacao_data (cls, data):

        formato = "%d/%m/%Y"

        data = datetime.strptime(data, formato)

        return data

    @field_validator ("status")
    def validacao_status (cls, status) -> str:

        status = status.title().strip()

        if status not in ['Entregue', 'Enviado', 'Processando']:
            raise ValueError('Status do pedido inválido.')

        return status