import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period =  Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    superface_water = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passagers = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumable = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    max_atmosphering_speed = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    passagers = Column(String(250), nullable=False)
    cargo_capacity = Column(String(250), nullable=False)
    consumable = Column(String(250), nullable=False)
    vehicle_class  = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    designation = Column(String(250), nullable=False)
    average_height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    usuario = relationship(Usuario)
    planets = relationship(Planets)
    people = relationship(People)
    starship = relationship(Starship)
    vehicle = relationship(Vehicle)
    species = relationship(Species)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
