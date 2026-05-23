from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models.ordem import Base, OrdemServico
from app.schemas.ordem import OrdemCreate, OrdemConcluir

# Base.metadata.create_all(bind=engine)

app = FastAPI(title="iFix Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/ordens")
def criar_ordem(ordem: OrdemCreate, db: Session = Depends(get_db)):
    nova_ordem = OrdemServico(
        cliente=ordem.cliente,
        aparelho=ordem.aparelho,
        defeito=ordem.defeito
    )
    db.add(nova_ordem)
    db.commit()
    db.refresh(nova_ordem)
    return {"mensagem": "OS criada com sucesso!", "dados": nova_ordem}

@app.get("/ordens")
def listar_ordens(db: Session = Depends(get_db)):
    ordens = db.query(OrdemServico).all()
    return ordens


@app.put("/ordens/{ordem_id}/concluir")
def concluir_ordem(ordem_id: int, dados: OrdemConcluir, db: Session = Depends(get_db)):
    ordem = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    
    if not ordem:
        return {"erro": "Ordem não encontrada"}
        
    ordem.status = "Concluída"
    ordem.valor = dados.valor 
    db.commit()
    db.refresh(ordem)
    
    return {"mensagem": "Ordem concluída com sucesso!", "dados": ordem}

@app.delete("/ordens/{ordem_id}")
def deletar_ordem(ordem_id: int, db: Session = Depends(get_db)):
    ordem = db.query(OrdemServico).filter(OrdemServico.id == ordem_id).first()
    if not ordem:
        return {"erro": "Ordem não encontrada"}
    db.delete(ordem)
    db.commit()
    return {"mensagem": "Ordem deletada com sucesso!"}