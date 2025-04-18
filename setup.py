from setuptools import find_packages, setup

setup(
    name='CAREAI',
    version='0.0.0',
    author='Aryan Kumar',
    author_email='aryankumar725018@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[]
)
