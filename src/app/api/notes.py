from app.api import crud
from app.api.schema import NoteSchema, NoteDB
from fastapi import APIRouter


router = APIRouter()


@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }

    return response_object
