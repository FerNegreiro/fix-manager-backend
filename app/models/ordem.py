from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OrdemServico(Base):
    __tablename__ = "ordens"

    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String)
    aparelho = Column(String)
    defeito = Column(String)
    status = Column(String, default="Aberta")
    valor = Column(Float, default=0.0) 