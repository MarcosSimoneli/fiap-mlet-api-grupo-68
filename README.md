# Api Embrapa Grupo 68

Essa é uma API que disponibiliza dados de vitivinicultura da Embrapa.

## Estrutura do Projeto

```
my-fastapi-app
├── src
│   ├── main.py              # Ponto de entrada da aplicação FastAPI
│   └── routes
│       ├── health_check.py  # Rota para checar se a aplicação está saudável
│       ├── comercio.py      # Define rota que expõe os dados do comércio
│       ├── exportacao.py    # Define rota que expõe os dados de exportação
│       ├── importacao.py    # Define rota que expõe os dados de importação
│       ├── processamento.py # Define rota que expõe os dados de processamentos
│       └── producao.py      # Define rota que expõe os dados de produção
├── requirements.txt         # Lista as dependências do projeto
└── README.md                # Documentação do projeto
```

## Requisitos

Para executar esta aplicação, você precisa ter Python instalado junto com as seguintes dependências:

- FastAPI
- Uvicorn

Você pode instalar os pacotes necessários usando pip:

```
pip install -r requirements.txt
```

## Executando a Aplicação

Para iniciar a aplicação FastAPI, navegue até o diretório `src` e execute:

```
uvicorn main:app --reload
```

Isso iniciará o servidor, e você poderá acessar a aplicação em `http://127.0.0.1:8000`.

## Acessando a API

Uma vez que o servidor esteja em execução, você pode acessar os seguintes endpoints:

- `GET /healh check`: Retorna uma mensagem "Ok".
- `GET /embrapa/processamento/viniferas`: Retorna dados sobre viníferas.
- `GET /embrapa/processamento/americanasHibridas`: Retorna dados sobre americanas e híbridas.
- `GET /embrapa/processamento/uvasDeMesa`: Retorna dados sobre uvas de mesa.
- `GET /embrapa/processamento/semClassificacao`: Retorna dados sobre sem classificação.
- `GET /embrapa/producao`: Retorna dados sobre produção.
- `GET /embrapa/comercio`: Retorna dados sobre comércio.
- `GET /embrapa/importacao`: Retorna dados sobre importação.
- `GET /embrapa/exportacao`: Retorna dados sobre exportação.

## Licença

Este projeto está licenciado sob a Licença MIT.
