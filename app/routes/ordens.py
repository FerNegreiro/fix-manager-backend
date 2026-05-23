
from fastapi import APIRouter

router = APIRouter(prefix="/ordens", tags=["Ordens"])

@router.get("/")
def listar_ordens():
    return [
        {
            "cliente": "Fernando",
            "aparelho": "iPhone 13",
            "status": "Em manutenção"
        }
    ]
