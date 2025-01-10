from fastapi import APIRouter
import requests
import pandas as pd
from io import StringIO
import json

router = APIRouter()

@router.get("/viniferas")
async def read_root():
    url = r"http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv"
    response = requests.get(url)
    
    csv_content = response.content.decode('utf-8')
    
    df = pd.read_csv(StringIO(csv_content), delimiter=';')
    
    json_data = df.to_json(orient="records")
    
    result = {"viniferas": json.loads(json_data)}

    return result

@router.get("/americanasHibridas")
async def read_root():
    url = r"http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv"
    response = requests.get(url)
    
    csv_content = response.content.decode('utf-8')
    
    df = pd.read_csv(StringIO(csv_content), delimiter=';')
    
    json_data = df.to_json(orient="records")
    
    result = {"americana e hibridas": json.loads(json_data)}

    return result

@router.get("/uvasDeMesa")
async def read_root():
    url = r"http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv"
    response = requests.get(url)
    
    csv_content = response.content.decode('utf-8')
    
    df = pd.read_csv(StringIO(csv_content), delimiter=';')
    
    json_data = df.to_json(orient="records")
    
    result = {"uvas de mesa": json.loads(json_data)}

    return result

@router.get("/semClassificacao")
async def read_root():
    url = r"http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv"
    response = requests.get(url)
    
    csv_content = response.content.decode('utf-8')
    
    df = pd.read_csv(StringIO(csv_content), delimiter=';')
    
    json_data = df.to_json(orient="records")
    
    result = {"sem classificacao": json.loads(json_data)}

    return result

def register_routes(app):
    app.include_router(router)