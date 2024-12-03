# Pytest

## What is Pytest?

- Testing framework for Python
- Auto-discovery-of tests
- Rich assertion introspection
- Support parameterized and fixture-based testing

## Why Pytest?

- Simplified syntax
- Rich assertion introspection
- Powerful fixture system
- Compatibility
- Extensibility

## Environment setup

```terminal
# clone the repo
$ git clone https://github.com/matthiasdroth/Pytest_tutorial_freecodecamp.git
# navigate into the repo
$ cd Pytest_tutorial_freecodecamp
# create a virtual environment
$ python -m venv env # or python3 -m venv env, depending on your python setup
# activate the environment
$ source env/bin/activate
# install the dependencies
$ pip install -r requirements.txt
```

```terminal
# deactivate the environment
$ deactivate
```

## Commands for running Pytest

`tests$ pytest test_square.py` (vanilla)
`tests$ pytest -v test_square.py` (verbose)

It may be necessary to set the `PYTHONPATH` environment variable in the following fashion:
`$ export PYTHONPATH=/your/local/path/to/Pytest_tutorial_freecodecamp:$PYTHONPATH`

For further information on `PYTHONPATH`, check the file `PYTHONPATH_tutorial.txt`.
