from cx_Freeze import setup, Executable

setup(name = 'coursework',
      version='0.1',
      description='course work ',
      executables = [Executable('main.py')])