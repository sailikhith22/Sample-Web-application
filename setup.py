from setuptools import find_packages, setup
from typing import List

trigger = "-e ."
def get_requirements(file_path:str)->List[str]:
    """Returns the list of requirements mentioned in the requirements function"""
    requirements=[]
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [requirement.replace("\n","") for requirement in requirements]
    if trigger in requirements:
        requirements.remove(trigger)
    return requirements
setup(
    name="Projects_01" , 
    version="0.0.1",
    author="Maheshbabu",
    author_email="maheshbabu9199@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)