from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Octavioomg",
    author_email="octavioomg@outlook.com.br",
    description="Pacote de Processamento de Imagem em Python",
    long_description="O pacote identifica semelhança entre imagens e também cria nova imagem a partir de duas, com similaridade entre elas. Gera uma imagem a partir de duas existentes",
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)