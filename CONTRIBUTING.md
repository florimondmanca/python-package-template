# Contributing guidelines

Hi! Glad to see that you are interested in contributing to this project.

## Getting started

Here's how to get up and running:

- Make sure you have a working installation of [Python](https://www.python.org/) 3.6+.
- Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Run the tests:

```bash
pytest
```

Once tests pass locally, feel free to work on a separate branch and open a pull request whenever you'd like to receive review.

## Code quality

- Black is installed along with development dependencies. We encourage you to configure your IDE to automatically run Black on file save. You can run it manually using:

```bash
black thepackage tests
```

- Static type checking is done using `mypy`. All type checks must pass for CI to succeed. You can run static type checks locally using:

```bash
mypy thepackage
```
