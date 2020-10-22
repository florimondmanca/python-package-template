# python-package-template

My opinionated [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for Python packages.

## Quickstart

Install `cookiecutter`, then:

```bash
cookiecutter https://github.com/florimondmanca/python-package-template
```

## Usage

### Scripts

The `scripts/` directory contains reusable and standardized scripts that fit the following workflow:

* `scripts/install` - Install development environment.
* `scripts/test` - Run the test suite.
* `scripts/lint` - Run code formatting.
* `scripts/check` - Check code quality.
* `scripts/build` - Build package assets.
* `scripts/publish` - Publish package to PyPI.

These scripts is how I interact with all my packages, ensuring a standardized and streamlined workflow everywhere. (You may add more scripts as seem fit: `scripts/docs`, `scripts/serve`, etc.)

### Top-level files

This template comes with a few top-level files:

* `setup.py` - Python package [setup script](https://docs.python.org/3/distutils/setupscript.html).
* `setup.cfg` - Configuration for tools: linters, formatters, test framework, etc. (Note: increasingly more projects switch to `pyproject.toml` — I'm still a bit old school, YMMV.)
* `requirements.txt` - List of development dependencies (used by `scripts/install`).
* `MANIFEST.in` - A Python package manifest file. Typically meant to remain unchanged for pure-Python packages (e.g. no C extensions).
* `CHANGELOG.md` - A changelog file where changes to the project can be recorded.
* `LICENSE` - Project license. This template uses MIT, but feel free to change the license to something else. ([mklicense](https://github.com/cezaraugusto/mklicense) may be handy.)
* `.gitignore` - List of files to be ignored by Git.

### Code layout

This package uses an [`src` layout](https://hynek.me/articles/testing-packaging/). (The package code is inside an `src/<package-name>` directory, rather than a top-level `<package-name>` directory. This is so that the package is installed like any other PyPI package during development, rather than as a local directory, making sure the installation of the package itself is also tested, so that any installation issues are caught early on rather than when users install the package from PyPI. If this doesn't mean a lot to you, don't sweat it. :))

### CI

The `ci/` directory contains an `azure-pipelines.yml` file, which is a configuration file for Azure Pipelines. This file contains a reference to my [azure-pipelines-templates](https://github.com/florimondmanca/azure-pipelines-templates) where I host standardized steps and jobs based on the standard scripts defined above.

This template also adds a "build status" badge pointing at the Azure Pipelines page. This is what the `azure_definition_id` cookiecutter option is for.

Feel free to change or remove this directory if you use a different CI provider, or if you don't use CI at all.

### Miscellaneous

* This template has a [Codecov](https://codecov.io/) badge on the README. Feel free to remove it if you don't use this service.
* This template [enables Dependabot](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/enabling-and-disabling-version-updates#enabling-github-dependabot-version-updates) to send updates of dependencies found in `requirements.txt` on a monthly basis.

## License

MIT
