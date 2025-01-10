from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

def register_routes(app):
    app.include_router(router)