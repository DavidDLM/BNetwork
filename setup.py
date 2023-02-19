import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bayes Networks",                  # This is the name of the package
    version="0.0.1",                        # The initial release version
    author="MDL",                     # Full name of the author
    description="Bayes Networks for Building and calculating Bayes Networks",
    # Long description read from the the readme file
    long_description=long_description,
    long_description_content_type="text/markdown",
    # List of all python modules to be installed
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["Bayes Networks"],             # Name of the python package
    # Directory of the source code of the package
    url="https://github.com/DavidDLM/BNetwork",
    install_requires=[]                     # Install other dependencies if any
)
