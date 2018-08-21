import setuptools

setuptools.setup(
    name="csv2any",
    version="0.1.1",
    url="https://github.com/karimov/csv2any",

    author="Davron Karimov",
    author_email="davron.sh.karimov@gmail.com",

    description="A tool that converts the data from one format to other formats.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=["click"],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5+',
    ],
    entry_points={
        'console_scripts': [
            'csv2any = csv2any.cli:main'
        ]
    }

)
