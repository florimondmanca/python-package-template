import re
from pathlib import Path

from setuptools import find_packages, setup


def get_version(package: str) -> str:
    version = (Path("src") / package / "__version__.py").read_text()
    match = re.search("__version__ = ['\"]([^'\"]+)['\"]", version)
    assert match is not None
    return match.group(1)


def get_long_description() -> str:
    with open("README.md", encoding="utf8") as readme:
        with open("CHANGELOG.md", encoding="utf8") as changelog:
            return readme.read() + "\n\n" + changelog.read()


setup(
    name="{{ cookiecutter.package_slug }}",
    version=get_version("{{ cookiecutter.package_name }}"),
    description="{{ cookiecutter.package_short_description }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="http://github.com/{{ cookiecutter.author_github_username }}/{{ cookiecutter.package_slug }}",
    author="{{ cookiecutter.author_full_name }}",
    author_email="{{ cookiecutter.author_email }}",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    python_requires=">={{ cookiecutter.python_min_version }}",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: {{ cookiecutter.python_min_version }}",
    ],
)
