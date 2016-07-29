import setuptools

setuptools.setup(
    name='windows-multiprocessing-bug',
    version='1.0.0',
    license='MIT',
    description='Small reproduction case for Windows multiprocessing bug',
    long_description='',
    author='Ian Cordasco',
    author_email='graffatcolmingov@gmail.com',
    url='https://github.com/sigmavirus24/windows-multiprocessing-bug',
    package_dir={'': 'src'},
    packages=['repro'],
    install_requires=['mccabe'],
    entry_points={
        'console_scripts': [
            'run-multiprocessing-test = repro.main:main',
        ],
    },
    classifiers=[
        'Framework :: Flake8',
    ],
)
