import uvicorn
from fastapi import FastAPI

from controlador_produto import router as produto_router
from controlador_cliente import router as cliente_router
from controlador_pedidos import router as pedidos_router
from controlador_marcas import router as marcas_router

app = FastAPI()

app.include_router (produto_router)
app.include_router (cliente_router)
app.include_router (pedidos_router)
app.include_router (marcas_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload = True
    )