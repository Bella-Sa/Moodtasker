from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import traceback

from app.database import get_db
from app.controllers.agenda_tarefa_controller import AgendaTarefaController
from app.dtos.agenda_tarefa_dto import AgendaTarefaCreate, AgendaTarefaUpdate, AgendaTarefaRead

router = APIRouter(tags=["Agenda Tarefas"])

#@router.get("/", response_model=List[AgendaTarefaRead])
#def listar_agenda_tarefas(db: Session = Depends(get_db)):
 #   return AgendaTarefaController(db).listar()

@router.get("/", response_model=List[AgendaTarefaRead])
def listar_agenda_tarefas(db: Session = Depends(get_db)):
    try:
        return AgendaTarefaController(db).listar()
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

#@router.get("/{agenda_id}", response_model=AgendaTarefaRead)
#def buscar_agenda_tarefa(agenda_id: int, db: Session = Depends(get_db)):
 #   agenda = AgendaTarefaController(db).buscar(agenda_id)
  #  if not agenda:
   #     raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")
    #return agenda

@router.get("/{agenda_id}", response_model=AgendaTarefaRead)
def buscar_agenda_tarefa(agenda_id: int, db: Session = Depends(get_db)):
    try:
        agenda = AgendaTarefaController(db).buscar(agenda_id)
        if not agenda:
            raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")
        return agenda
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

#@router.post("/", response_model=AgendaTarefaRead, status_code=status.HTTP_201_CREATED)
#def criar_agenda_tarefa(agenda_create: AgendaTarefaCreate, db: Session = Depends(get_db)):
 #   return AgendaTarefaController(db).criar(agenda_create)

@router.post("/", response_model=AgendaTarefaRead, status_code=status.HTTP_201_CREATED)
def criar_agenda_tarefa(agenda_create: AgendaTarefaCreate, db: Session = Depends(get_db)):
    try:
        return AgendaTarefaController(db).criar(agenda_create)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

#@router.put("/{agenda_id}", response_model=AgendaTarefaRead)
#def atualizar_agenda_tarefa(agenda_id: int, agenda_update: AgendaTarefaUpdate, db: Session = Depends(get_db)):
 #   agenda = AgendaTarefaController(db).atualizar(agenda_id, agenda_update)
  #  if not agenda:
   #     raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")
    #return agenda

@router.put("/{agenda_id}", response_model=AgendaTarefaRead)
def atualizar_agenda_tarefa(agenda_id: int, agenda_update: AgendaTarefaUpdate, db: Session = Depends(get_db)):
    try:
        agenda = AgendaTarefaController(db).atualizar(agenda_id, agenda_update)
        if not agenda:
            raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")
        return agenda
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

#@router.delete("/{agenda_id}", status_code=status.HTTP_204_NO_CONTENT)
#def deletar_agenda_tarefa(agenda_id: int, db: Session = Depends(get_db)):
 #   sucesso = AgendaTarefaController(db).deletar(agenda_id)
  #  if not sucesso:
   #     raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")

@router.delete("/{agenda_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_agenda_tarefa(agenda_id: int, db: Session = Depends(get_db)):
    try:
        sucesso = AgendaTarefaController(db).deletar(agenda_id)
        if not sucesso:
            raise HTTPException(status_code=404, detail="Agenda Tarefa não encontrada")
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")