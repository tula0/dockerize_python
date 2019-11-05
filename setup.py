from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='docker_imgs_temp',
   version='1.0',
   description='This Package helps create a scaffolding of docker images. It also offer an interface for working with docker',
   license="MIT",
   long_description=long_description,
   author='Lukio',
   author_email='lukio.olweny@gmail.com',
   url="http://www.foopackage.com/",
   packages=['foo'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/script1',
            'scripts/script2',
           ]
)

#publish the package into PyPI:
! python setup.py register #register the package name in the PyPI
! python setup.py upload 
! python setup.py --sign upload #sign your package with GPG


#install package on any other computer:
! pip install yourpackage
