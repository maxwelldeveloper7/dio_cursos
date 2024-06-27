from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='12345678900', max_lenth=11)]
    idade: Annotated[str, Field(description='idade do atleta', example='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', example=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example=1.7)]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_lenth=1)]
