from app.api.schema import NoteSchema
from app.models import notes
from app.db import database


async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)
