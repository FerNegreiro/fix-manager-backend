from pydantic import BaseModel

class OrdemCreate(BaseModel):
    cliente: str
    aparelho: str
    defeito: str


class OrdemConcluir(BaseModel):
    valor: float