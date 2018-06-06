import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typy_checker",
    version="0.4",
    author="Santosh Venkatraman",
    author_email="santosh.venk@gmail.com",
    description="Type Checking Function Arguments for Humans™",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/onstash/typy_checker",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
