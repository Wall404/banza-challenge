from fastapi import FastAPI
from config.openapi import tags_metadata
from routes.cliente import cliente

app = FastAPI(
    title="Banza-Challenge API",
    description="a REST API using python and mysql",
    version="0.0.1",
    openapi_tags=tags_metadata,)

app.include_router(cliente)
