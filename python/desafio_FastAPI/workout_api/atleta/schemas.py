from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='João', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta', examples='12345678900', max_lenth=11)]
    idade: Annotated[str, Field(description='idade do atleta', examples='25')]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', examples=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', examples=1.7)]
    sexo: Annotated[str, Field(description='Sexo do atleta', examples='M', max_lenth=1)]
