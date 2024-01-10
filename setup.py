import setuptools

with open("./README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plopy",
    version="1.6.9",
    author="Finnventor",
    description="GUI for matplotlib graphing",
    long_description=long_description,
    url="https://github.com/Finnventor/plopy",
    packages=setuptools.find_packages(),
    package_data={'plopy': ['*.txt'], 'plopy.ui': ['*.png']},
    install_requires=['python-dateutil>=2.8.1', 'PySide6-Essentials', 'matplotlib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ]
)
