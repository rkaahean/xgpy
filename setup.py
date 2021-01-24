import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


# reading in the requirements
# from requirements.txt file
thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="xgpy", # Replace with your own username
    version="0.0.2",
    author="Ranjan Srinivas",
    author_email="ranjan310151997@gmail.com",
    description="A Python package to fetch football data from multiple sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkaahean/xgpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = install_requires
)
