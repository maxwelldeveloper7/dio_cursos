from typing import Annotated
from pydantic import BaseModel, Field


class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do atleta', examples='João', max_length=50)]
# TODO continuar apartir de 8:19 --> Criação de schemas e models - Entidade Atleta