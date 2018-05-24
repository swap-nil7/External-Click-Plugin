"""
Setup script for `PrintItStyle`
"""


from setuptools import setup


setup(
    name='ext_plugin',
    version='0.1dev0',
    py_modules=['core'],
    entry_points='''
        [main.plugins]
        color=core:color
    '''
)

