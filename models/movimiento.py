from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DECIMAL, DateTime
from config.db import meta, engine

cuenta = Table("movimientos", meta,
               Column("id", Integer, primary_key=True, autoincrement=True),
               Column("id_cuenta", Integer),
               Column("tipo", String(255)),
               Column("importe", DECIMAL),
               Column("fecha", DateTime))

meta.create_all(engine)