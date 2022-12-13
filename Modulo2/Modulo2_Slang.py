from sqlalchemy import Column, String, Integer
from Modulo2 import Base

class Slang(Base):
    __tablename__ = 'tbl_slang'

    id = Column(Integer, primary_key=True)
    palabra = Column(String(100))
    significado = Column(String(255))

    def __init__(self,palabra,significado):
        self.palabra = palabra
        self.significado = significado
