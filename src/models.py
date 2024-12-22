import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)



class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

class Planets_Favorites(Base):
    __tablename__ = 'planets_favorites'
    PlanetFavoritesID = Column(Integer, primary_key=True)
    UserID = Column(String(250), ForeignKey("user.id"))
    PlanetId = Column(Integer, ForeignKey('planets.id'))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)

class Vehicles_Favorites(Base):
    __tablename__ = 'vehicles_favorites'
    VehiclesFavoritesID = Column(Integer, primary_key=True)
    UserID = Column(String(250), ForeignKey("user.id"))
    VehicleId = Column(Integer, ForeignKey('vehicles.id'))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)

class Characters_Favorites(Base):
    __tablename__ = 'characters_favorites'
    CharacterFavoritesID = Column(Integer, primary_key=True)
    UserID = Column(String(250), ForeignKey("user.id"))
    CharactertId = Column(Integer, ForeignKey('characters.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
