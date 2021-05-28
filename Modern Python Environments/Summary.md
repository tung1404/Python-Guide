
# **Modern Python Environments - dependency and workspace management**

# Installing Python

We recommend installing Python with pyenv.

The build dependencies vary by platform:

###  Ubuntu/Debian

```bash
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```
### Alpine

```
apk add --no-cache git bash build-base libffi-dev openssl-dev bzip2-dev zlib-dev \
readline-dev sqlite-dev 
```

### Using the pyenv-installer

After you’ve installed the build dependencies, you’re ready to install pyenv itself.
Using the pyenv-installer project:


```bash
$ curl https://pyenv.run | bash
```

Add to ~/.profile

```bash
# Add pyenv executable to PATH and
# enable shims by adding the following
# to ~/.profile:

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

# Installing Python

Once installed, you can easily install a specific version of Python like so:

```bash
$ pyenv install 3.9.5
$ pyenv versions
```

# Managing Dependencies

## venv + pip

venv and pip (package installer for python), which come pre-installed with most versions of Python, are the most popular tools for managing virtual environments and packages, respectively. They are fairly simple to use.

```bash
python -m venv my_venv
source my_venv/bin/activate
# to deactivate enviroment
deactivate

python -m pip freeze > requirements.txt
```

*requirements-dev.txt:*

```
# prod
-r requirements.txt

# dev
black==20.8b1
coverage==5.0.3
flake8==3.7.9
ipython==7.12.0
isort==4.3.21
pytest-django==3.8.0
pytest-cov==2.8.1
pytest-xdist==1.31.0
pytest-mock==3.1.1
```

## Poetry

Poetry is arguably the most feature-rich dependency management tool for Python. It comes with a powerful CLI used for creating and managing Python projects.
> Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies.

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
``` 

Once installed, to scaffold a new project run:

```bash
$ poetry new sample-project
$ cd sample-project
$ tree ./sample-project/

./sample-project/
├── README.rst
├── pyproject.toml
├── sample_project
│   └── __init__.py
└── tests
    ├── __init__.py
    └── test_sample_project.py

3 directories, 6 files
```

Dependencies are managed inside the pyproject.toml file:

```bash
$ cat ./sample-project/pyproject.toml 
``` 
```toml
[tool.poetry]
name = "sample-project"
version = "0.1.0"
description = ""
authors = ["Daniel Cruz <adm.dcf@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

To add new a dependency, simply run:

```bash
# The --dev flag indicates that the dependency is meant to be used in development mode only. Development dependencies are not installed by default.

poetry add [--dev] <package name>
```

For example:
```bash
$ poetry add flask
$ poetry add --dev black
```

```toml
[tool.poetry.dependencies]
python = "^3.8"
Flask = "^2.0.1"

[tool.poetry.dev-dependencies]
pytest = "^5.2"
black = "^21.5b1"
```
*[Version constraints](https://python-poetry.org/docs/versions/)*

```Flask = "^2.0.1"``` means  that the versions  allowed are ```>=2.0.1 <3.0.0```

```poetry run <command>``` will run commands inside the virtual environment.

To activate it run ```poetry shell```, to deactivate it run ```exit```:

```bash
$ poetry shell
(env) $ exit
```
[Managing environments with poetry](https://python-poetry.org/docs/managing-environments/)

## Pipenv

[Pipenv](https://docs.pipenv.org/) attempts to solve the same problems that Poetry does.

## Recommendations

Notes:

1. Publishing to PyPI is much easier with Poetry, so if you're creating a Python package go with Poetry.

2. Both projects (Poetry and Pipenv) are fairly slow when it comes to dependency resolution, so if you're using Docker you may want to steer clear of them both.

3. From an open-source development perspective, Poetry moves faster and is arguably more responsive to user feedback.