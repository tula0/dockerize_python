import sys
print(sys.path)
sys.path.append(r'E:\analytics\webapps')
sys.path.append(r'E:\analytics\webapps\docker_imgs_temp')
print(f'Invoking __init__.py for {__name__}')
A = ['quux', 'corge', 'grault']

#initializes package-level data

#modules to be imported when "from pkg import *" is invoked
__all__ = [
        'calc',
        'dummy_routines'
        ]