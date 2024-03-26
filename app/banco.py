from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime
from datetime import datetime

engine = create_engine('sqlite:///pesquisa_ip.db', echo=True)

print("Conexão com SQLite estabelecida.")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'tbl_resultado_bgp'
    
    result = Column(String, primary_key=True)
    type = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)