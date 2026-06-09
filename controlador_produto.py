from fastapi import APIRouter
from sqlalchemy import create_engine, text
from produto import Produto

router = APIRouter(prefix="/produto", tags=["Produtos"])

DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@router.post('/')
def cadastrar (produto: Produto):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.produtos (nome_produto, preco, estoque, marca_id)
                VALUES ( :nome, :preco, :estoque, :marca_id)
                  """ 
                       
            dados = {
                "nome" : produto.nome_produto,
                "preco" : produto.preco,
                "estoque" : produto.estoque,
                "marca_id" : produto.marca_id
            }

            con.execute(text(sql), dados)

            engine.dispose()
    except Exception as e:
        return e

@router.delete('/{id}')
def deletar(id:int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                DELETE FROM public.produto
	            WHERE id = :id
                  """  
                      
            dados = {
                "id" : id
            }

            con.execute(text(sql), dados)

            engine.dispose()

            return 'Apagado com sucesso'
        
    except Exception as e:
        return e

@router.put('/{id}')
def atualizar(id:int, produto: Produto):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                UPDATE public.produto
	            SET nome = :nomeNovo, valor=:valorNovo
                WHERE id=:id
	              """            
            
            dados = {
                "nomeNovo" : produto.nome_produto,
                "valorNovo" : produto.preco,
                'id': id
            }

            con.execute(text(sql), dados)

            engine.dispose()

            return 'atualizado com sucesso'
        
    except Exception as e:
        return e

@router.get("/{id}")
def buscar(id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:

            sql = """
                SELECT p.id, p.nome_produto, p.preco FROM produtos p
                WHERE p.id = :id
                  """
            
            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)
            produto = resultado.fetchone()

            return produto._mapping
            
    except:
        return "erro no banco"

@router.get('/listar')
def listar():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """
                    SELECT p.id, p.nome_produto, p.preco FROM produtos p 
                  """
            
            resultado = con.execute(text(sql))
            linhas_do_banco = resultado.fetchall()

            produtos = []

            for row in linhas_do_banco:
                linha = row._mapping

                produto = {
                    "id": linha['id'],
                    "preco": linha ['preco'],
                    "nome": linha['nome_produto'] 
                }

                produtos.append(produto)

            return produtos 
            
    except Exception as e:
        return f"erro no banco {e}"
    
@router.get('/{pais}')
def listar_por_pais(pais):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """
                    SELECT p.id, p.nome_produto, p.preco, m.nome_marca, m.pais_origem
                    FROM produtos p
                    JOIN marcas m ON p.marca_id = m.id
                    WHERE m.pais_origem = :paisBanco 
                  """

            dados = {
                "paisBanco": pais
            }

            resultado = con.execute(text(sql), dados)
            linhas_do_banco = resultado.fetchall()

            produtos = []

            for row in linhas_do_banco:
                linha = row._mapping

                produto = {
                    "id": linha['id'],
                    "preco": linha['valor'],
                    "nome": linha['nome'],
                    "marca": {
                        "nome": linha['nome_marca'],
                        "pais": linha['pais_origem']
                    }                                   
                }

                produtos.append(produto)

            return produtos 
            
    except:
        return "erro ao recuperar seus dados"

@router.get('/{valor}')
def listar_por_maior_valor(valor):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql ="""
                SELECT p.nome_produto, m.nome_marca, p.preco
                FROM produtos p
                INNER JOIN marcas m ON m.id = p.marca_id
                WHERE p.preco > :valor
                 """

            dados = {
                "valor": valor
            }

            resultado = con.execute(text(sql), dados)
            linhas_do_banco = resultado.fetchall()

            produtos = []

            for row in linhas_do_banco:
                linha = row._mapping

                produto = {
                    "nome": linha['nome'],
                    "preco": linha['valor'],
                    "marca": linha['nome_marca']       
                }

                produtos.append(produto)

            return produtos 
            
    except:
        return "erro no banco"
