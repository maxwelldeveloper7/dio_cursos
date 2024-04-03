from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="formatbr",
    version="0.0.1",
    author="Maxwell de Oliveira Chaves",
    author_email="maxwellchaves1844@gmail.com",
    description="This module offers tools for data formatting.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxwelldeveloper7/dio_cursos/tree/main/python/tratamento_de_dados/criacao_de_pacotes/FormatBr",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
