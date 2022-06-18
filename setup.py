from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME='HOUSING-PREDICTOR'
VERSION="0.0.3",
AUTHOR="Pallabi Sahoo"
DESCRIPTION="This is a house price prediction project"
REQUIREMETS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return anlist which contain name
    of libraries mentioned in requirements.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file

    """
    
    with open(REQUIREMETS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

