from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'  # Correct variable name

def get_requirements(file_path: str) -> List[str]:
    ''' this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Correct usage of variable name

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='manideep',
    author_email='manideepmaddileti@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn']  # This line is commented out now.
    install_requires=get_requirements('requirements.txt')
)
