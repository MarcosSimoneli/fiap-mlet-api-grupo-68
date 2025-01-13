from fastapi import FastAPI
from routes.hello import router as hello_router
from routes.processamento import router as processamento_router
from routes.producao import router as producao_router
from routes.comercio import router as comercio_router

def create_app():
    app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
    app.include_router(hello_router, prefix="/hello")
    app.include_router(processamento_router, prefix="/embrapa/processamento")
    app.include_router(producao_router, prefix="/embrapa/producao")
    app.include_router(comercio_router, prefix="/embrapa/comercio")
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)