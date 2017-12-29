from setuptools import setup, find_packages


setup(
    name='yeezy',
    description='Kanye West-based pass phrase generator',
    author='Carl Bordum Hansen',
    version='0.1',
    license='MIT',
    url='https://github.com/Zaab1t/yeezy',
    py_modules=['yeezy'],
    entry_points={
        'console_scripts': ['yeezy=yeezy:main'],
    },
    data_files=[('', ['kanye_verses.txt'])],
)
