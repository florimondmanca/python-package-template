from pathlib import Path

from setuptools import find_packages, setup

with open(str(Path(".") / "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

REQUIREMENTS_CI = ["pytest", "pytest-cov", "codecov", "mypy"]
REQUIREMENTS_DEV = [*REQUIREMENTS_CI, "black", "pylint", "rope", "bumpversion"]

setup(
    name="thepackage",
    version="0.0.0",
    author="Florimond Manca",
    author_email="florimond.manca@gmail.com",
    description="thedescription",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/florimondmanca/thepackage.git",
    packages=find_packages(exclude=["tests*"]),
    package_data={"thepackage": ["py.typed"]},
    zip_safe=False,
    install_requires=[],
    extras_require={"dev": REQUIREMENTS_DEV, "ci": REQUIREMENTS_CI},
    python_requires=">=3.6",
    license="MIT",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
