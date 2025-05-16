from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

DBSession = scoped_session(sessionmaker())
Base = declarative_base()

class Matakuliah(Base):
    __tablename__ = 'matakuliah'
    
    id = Column(Integer, primary_key=True)
    kode = Column(String(10), unique=True, nullable=False)
    nama = Column(String(100), nullable=False)
    sks = Column(Integer, nullable=False)
    dosen = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Matakuliah(kode='{self.kode}', nama='{self.nama}', sks={self.sks}, dosen='{self.dosen}')>"
