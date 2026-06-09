from pydantic import BaseModel

class Pedidos (BaseModel):
    cliente_id: int
    data_pedido: str
    status: str