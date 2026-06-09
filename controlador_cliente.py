from fastapi import APIRouter
from sqlalchemy import create_engine, text
from cliente import Cliente

router = APIRouter(prefix="/cliente", tags=["Clientes"])

DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"
    
@router.post('/')
def cadastrar(cliente: Cliente):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.clientes (nome_cliente, email, cidade)
                VALUES ( :nomezinho, :email, :cidade)
                  """
                        
            dados = {
                "nomezinho" : cliente.nome,
                "email": cliente.email,
                "cidade": cliente.cidade
            }

            con.execute(text(sql), dados)

            engine.dispose()

    except Exception as e:
        return e

@router.get('/{id}')
def getOne (id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                SELECT * FROM public.clientes
                WHERE id = :id
                  """   
                     
            dados = {
                "id" : id
            }

            result = con.execute(text(sql), dados)
            cliente = result.fetchone()

            engine.dispose()

            if cliente:
                return {
                    "id": cliente.id,
                    "nome": cliente.nome_cliente,
                    "email": cliente.email,
                    "cidade": cliente.cidade
                }
            
            else:
                return {"message": "Cliente não encontrado"}

    except Exception as e:
        return e
    
@router.put('/')
def atualizar(cliente: Cliente):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                UPDATE public.clientes
                SET nome_cliente = :nomezinho,
                    email = :email,
                    cidade = :cidade
                WHERE id = :id
                  """    
                    
            dados = {
                "id": id,
                "nomezinho" : cliente.nome,
                "email": cliente.email,
                "cidade": cliente.cidade
            }

            con.execute(text(sql), dados)

            engine.dispose()

            return 'Cliente atualizado com sucesso'
        
    except Exception as e:
        return e
    
@router.delete('/{id}')
def deletar(id: int):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                DELETE FROM public.clientes
                WHERE id = :id
                  """
            
            dados = {
                "id" : id
            }

        con.execute(text(sql), dados)

        engine.dispose()

        return 'Cliente deletado com sucesso.'
    
    except Exception as e:
        return e