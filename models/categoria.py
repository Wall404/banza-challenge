from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

categoria = Table("categoria", meta, Column("id", Integer, primary_key=True), Column("nombre", String(255)))

meta.create_all(engine)