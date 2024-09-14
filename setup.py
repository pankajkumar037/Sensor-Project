from setuptools import find_packages,setup
from typing import List

h_e_dot='-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
    if h_e_dot in requirements:
        requirements.remove(h_e_dot)
    return requirements

setup(
    name="Fault detection",
    version="0.0.1",
    author="Pankaj",
    author_email="pankajkumarjnv76653@gmail.com",
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)