from setuptools import find_packages
from setuptools import setup

setup(
    name="PROJECT",
    version="1.0",
    description="DESCRIPTION",
    author="William Li",
    author_email="EMAIL",
    url="https://www.github.com",
    packages=find_packages(),
    install_reqs=[
        "black",
        "coverage",
        "mypy",
        "nox",
        "numpy",
        "pandas",
        "pdoc3",
        "pre-commit",
        "pylint",
        "pytest",
        "requests",
        "scalene",
        "tensorflow",
        "torch",
        "torchvision",
    ],
)
