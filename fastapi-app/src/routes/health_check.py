from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def health_check():
    return {"message": "Ok"}

def register_routes(app):
    app.include_router(router)