# python-package

[![build status](https://travis-ci.com/florimondmanca/python-package-template.svg?branch=master)](https://travis-ci.com/florimondmanca/python-package-template)
[![codecov](https://codecov.io/gh/florimondmanca/python-package-template/branch/master/graph/badge.svg)](https://codecov.io/gh/florimondmanca/python-package-template)
![license](https://img.shields.io/badge/license-MIT-green)

## Contents

- Python: 3.6+
- `setup.py`
- `requirements.txt`
- `.gitignore`
- Type hints: [PEP 561](https://www.python.org/dev/peps/pep-0561/)-compliant
- Tests: [pytest](https://docs.pytest.org/en/latest/)
- Code formatting: [Black](https://github.com/psf/black)
- Linting: pylint
- Type checking: mypy
- Refactoring: rope
- CI/CD: [Travis]
- Coverage reports: pytest-cov / [Codecov]
- Changelog: [Keep a Changelog](https://keepachangelog.com)
- Version bumping: bumpversion
- Contributing guidelines
- Code of conduct: [Contributor Covenant](https://www.contributor-covenant.org/)
- License: MIT

## Usage

- [Create a repo from this template](https://help.github.com/en/articles/creating-a-repository-from-a-template).
- Enable [Codecov] integration.
- Add `PYPI_USERNAME`, `PYPI_PASSWORD` and `CODECOV_TOKEN` to [Travis] settings.
- `git clone`
- Rename `thepackage` directory.
- Search and replace `thepackage`.
- Search and replace `thedescription`.
- Delete this README.
- Rename `README.tpl.md` as `README.md` and update its contents.
- `git push`
- `chmod +x tools/bumpversion.sh`
- `./tools/bumpversion.sh patch`
- `git push`
- `git push --tags`
- v0.0.1 released! 🚀

[travis]: https://travis-ci.com
[codecov]: https://codecov.io
