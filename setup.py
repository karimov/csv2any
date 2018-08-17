import setuptools

setuptools.setup(
    name="csv2any",
    version="0.1.0",
    url="https://github.com/karimov/csv2any",

    author="Davron Karimov",
    author_email="davron.sh.karimov@gmail.com",

    description="A tool that converts the data from one format to other formats.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
