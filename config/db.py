from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Configuración de la conexión a la base de datos
DATABASE_URL = "mysql+pymysql://root:123@localhost:3306/banzadb"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

