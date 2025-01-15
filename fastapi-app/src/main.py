from fastapi import Depends, FastAPI
from auth import validate_token, create_access_token
from pydantic import BaseModel
from routes.hello import router as hello_router
from routes.processamento import router as processamento_router
from routes.producao import router as producao_router
from routes.comercio import router as comercio_router
from routes.importacao import router as importacao_router
from routes.exportacao import router as exportacao_router
class TokenData(BaseModel):
    username: str
    password: str

def create_app():
    app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

    @app.post("/token")
    def generate_token(data: TokenData):
        token = create_access_token(data.dict())
        return {"access_token": token, "token_type": "bearer"}

    app.include_router(hello_router, prefix="/hello")
    app.include_router(processamento_router, prefix="/embrapa/processamento", dependencies=[Depends(validate_token)])
    app.include_router(producao_router, prefix="/embrapa/producao", dependencies=[Depends(validate_token)])
    app.include_router(comercio_router, prefix="/embrapa/comercio", dependencies=[Depends(validate_token)])
    app.include_router(importacao_router, prefix="/embrapa/importacao", dependencies=[Depends(validate_token)])
    app.include_router(exportacao_router, prefix="/embrapa/exportacao", dependencies=[Depends(validate_token)])
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)