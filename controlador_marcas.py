from fastapi import APIRouter
from sqlalchemy import create_engine, text
from marcas import Marcas

router = APIRouter(prefix="/marcas", tags=["Marcas"])

DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"