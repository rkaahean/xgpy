import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xgpy", # Replace with your own username
    version="0.0.1",
    author="Ranjan Srinivas",
    author_email="ranjan310151997@gmail.com",
    description="A Python package to fetch xG data from understat.",
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
    install_requires=[
        "pytest",
        "requests",
        "pandas"
    ]
)
