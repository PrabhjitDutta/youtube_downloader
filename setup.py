from setuptools import setup

setup(name='ytd',
      version='0.0.1',
      py_modules=['ytd'],
      install_requires=['requests', 'click', 'bs4', 'pytube'],
      entry_points='''
      [console_scripts]
      ytd = ytd:cli
      ''', 
      )
