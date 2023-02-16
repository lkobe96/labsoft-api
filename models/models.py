from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, UniqueConstraint
from database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    materiaUsuario = Column(String, nullable=False)
    raUsuario = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
   
class TipoUser(Base):
    __tablename__ = "tipousers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type_user = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    Id_Professor = Column(Integer, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Sala(Base):
    __tablename__ = "sala"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ativa = Column(Boolean, nullable=False)
    caixa_som = Column(Boolean, nullable=False)
    capacidade = Column(Integer, nullable=False)
    microfone = Column(Boolean, nullable=False)
    nome_sala = Column(String, nullable=False)
    projetor = Column(Boolean, nullable=False)
    computador = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Software(Base):
    __tablename__ = "softwares"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nomeSoftware = Column(String, nullable=False)
    licenca = Column(Boolean, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class SalaSoftware(Base):
    __tablename__ = "salasoftwares"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Id_sala = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Data = Column(DateTime(timezone=False))
    Quantidade_Alunos = Column(Integer, nullable=False)
    Id_sala = Column(Integer, nullable=False)
    Id_professor = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
