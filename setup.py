from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_luidi",
    version="0.0.1",
    author="Luidi_Carvalho",
    author_email="luidisilva2005@icloud.com",
    description="Minha primeira imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Luidisilva20/simple-package-template"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
