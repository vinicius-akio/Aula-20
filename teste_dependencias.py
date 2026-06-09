"""
Script de teste para validar todas as dependências da aplicação
"""

print("=" * 60)
print("TESTE DE DEPENDÊNCIAS - Aula 20")
print("=" * 60)

# Teste 1: Importação de FastAPI
try:
    import fastapi
    print(f"✓ FastAPI {fastapi.__version__} - OK")
except ImportError as e:
    print(f"✗ FastAPI - ERRO: {e}")

# Teste 2: Importação de Uvicorn
try:
    import uvicorn
    print(f"✓ Uvicorn {uvicorn.__version__} - OK")
except ImportError as e:
    print(f"✗ Uvicorn - ERRO: {e}")

# Teste 3: Importação de SQLAlchemy
try:
    import sqlalchemy
    print(f"✓ SQLAlchemy {sqlalchemy.__version__} - OK")
except ImportError as e:
    print(f"✗ SQLAlchemy - ERRO: {e}")

# Teste 4: Importação de psycopg2
try:
    import psycopg2
    print(f"✓ psycopg2 {psycopg2.__version__} - OK")
except ImportError as e:
    print(f"✗ psycopg2 - ERRO: {e}")

# Teste 5: Importação da aplicação main
print("\n" + "-" * 60)
print("Testando importação dos módulos da aplicação:")
print("-" * 60)

try:
    from main import app
    print(f"✓ main.py - OK")
    print(f"  Routers registrados: {len(app.routes)}")
except Exception as e:
    print(f"✗ main.py - ERRO: {e}")

# Teste 6: Teste de conexão com banco de dados
print("\n" + "-" * 60)
print("Testando conexão com PostgreSQL:")
print("-" * 60)

try:
    from sqlalchemy import create_engine, text
    DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"
    engine = create_engine(DATABASE_URL)
    
    with engine.begin() as con:
        con.execute(text("SELECT 1"))
    
    print("✓ Conexão PostgreSQL - OK")
    engine.dispose()
except Exception as e:
    print(f"✗ Conexão PostgreSQL - ERRO: {e}")
    print("  Verifique se o PostgreSQL está rodando e as credenciais estão corretas")

print("\n" + "=" * 60)
print("TESTE CONCLUÍDO")
print("=" * 60)
