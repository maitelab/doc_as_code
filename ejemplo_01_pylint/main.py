""" este codigo sirve para ...."""
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Ciudad(BaseModel):
    """ Esta clase guarda el objecto ciudad..... ...."""
    nombre: str
    pais: str

class CiudadesOutput(BaseModel):
    ciudades: List[Ciudad]

ciudad1 = Ciudad(nombre = "Lima", pais = "Perú")
ciudad2 = Ciudad(nombre = "Puerto Madryn", pais = "Argentina")
lista_ciudades = [ciudad1, ciudad2]

@app.get('/ciudades', response_model = CiudadesOutput, summary="Lista de ciudades", description="Obtener una lista de ciudades")
def get_cities():
    resultado = CiudadesOutput(ciudades = lista_ciudades)
    return resultado

@app.post('/ciudad', summary="Agregar ciudad", description="Adicionar una ciudad a la lista")
def create_city(input_data: Ciudad):
    lista_ciudades.append(input_data)
    return input_data
