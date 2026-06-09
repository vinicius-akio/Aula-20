from fastapi import APIRouter
from sqlalchemy import create_engine, text
from pedidos import Pedidos

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@router.get('/')
def listar_pedidos():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = '''
                SELECT nome_cliente, data_pedido, status
                FROM clientes c
                INNER join pedidos p
                ON c.id = p.cliente_id
                  '''            

            resultado = con.execute(text(sql))
   
            linhas_do_banco = resultado.fetchall()

            pedidos = []

            for row in linhas_do_banco:
                linha = row._mapping

                pedido = {
                    "Cliente": linha['nome_cliente'],
                    "Data do Pedido": linha['data_pedido'],
                    "Status": linha['status']
                }
                pedidos.append(pedido)

            engine.dispose()    

        return pedidos

    except Exception as e:
        return e

@router.get('/listar-por-nome')
def listar_pedidos_nome():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = '''
                SELECT nome_cliente, nome_produto, quantidade FROM clientes c
                INNER JOIN pedidos p ON c.id = p.cliente_id 
                INNER JOIN itens_compra ic ON p.id = ic.pedido_id
                INNER JOIN produtos pd ON pd.id = ic.produto_id
                  '''            

            resultado = con.execute(text(sql))
   
            linhas_do_banco = resultado.fetchall()

            pedidos_nome = []

            for row in linhas_do_banco:
                linha = row._mapping

                pedido_nome = {
                    "Cliente": linha['nome_cliente'],
                    "Produto": linha['nome_produto'],
                    "Quantidade": linha['quantidade']
                }
                pedidos_nome.append(pedido_nome)

            engine.dispose()    

        return pedidos_nome

    except Exception as e:
        return e

@router.get('/listar-valor-total')
def listar_pedidos_valor_total():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = '''
                SELECT
	                pr.nome_produto,
	                ic.quantidade,
                    ic.preco_unitario,
                    (ic.quantidade * ic.preco_unitario) AS total_pago
                FROM produtos pr
                INNER JOIN itens_compra ic
                ON pr.id = ic.produto_id;
                  '''            

            resultado = con.execute(text(sql))
   
            linhas_do_banco = resultado.fetchall()

            pedidos_valor_total = []

            for row in linhas_do_banco:
                linha = row._mapping

                pedido_valor_total = {
                    "Cliente": linha['nome_cliente'],
                    "Produto": linha['nome_produto'],
                    "Quantidade": linha['quantidade'],
                    "Preço Unitário": linha['preco_unitario'],
                    "Total Pago": linha['total_pago']
                }
                pedidos_valor_total.append(pedido_valor_total)

            engine.dispose()    

        return pedidos_valor_total

    except Exception as e:
        return e
    
@router.get('/listar-marcas-clientes')
def listar_marcas_clientes():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = '''
                SELECT 
                    m.nome_marca,
                    c.nome_cliente
                FROM clientes c
                INNER JOIN pedidos p
                    ON c.id = p.cliente_id
                INNER JOIN itens_compra ic
                    ON p.id = ic.pedido_id
                INNER JOIN produtos pr
                    ON ic.produto_id = pr.id
                INNER JOIN marcas m
                    ON pr.marca_id = m.id;
                  '''            

            resultado = con.execute(text(sql))
   
            linhas_do_banco = resultado.fetchall()

            listar_marcas_clientes = []

            for row in linhas_do_banco:
                linha = row._mapping

                marca_cliente = {
                    "Cliente": linha['nome_cliente'],
                    "Marca": linha['nome_marca'],
                }
                listar_marcas_clientes.append(marca_cliente)

            engine.dispose()    

        return listar_marcas_clientes

    except Exception as e:
        return e