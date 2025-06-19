from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    # Remove any leading/trailing whitespace and comments
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]
    
    return requirements


setup( 
    name="Fault detection",
    version="0.0.1",
    author="Pankaj Kumar",
    author_email="pankajkumarjnv76653@gmail.com",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)



"""
setuptools is a powerful library for packaging Python projects.

setup: The main function that declares metadata and configuration for the package.

find_packages(): Automatically finds all packages (directories with __init__.py) to include in the distribution.

"""