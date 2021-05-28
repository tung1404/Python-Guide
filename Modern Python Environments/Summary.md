
# Installing Python

We recommend installing Python with pyenv.

The build dependencies vary by platform:

###  Ubuntu/Debian

```shell
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


```shell
$ curl https://pyenv.run | bash
```

Add to ~/.profile

```shell
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

```shell
$ pyenv install 3.9.5
$ pyenv versions
```

# Managing Dependencies

## venv + pip

venv and pip (package installer for python), which come pre-installed with most versions of Python, are the most popular tools for managing virtual environments and packages, respectively. They are fairly simple to use.

```shell
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

# Poetry

Poetry is arguably the most feature-rich dependency management tool for Python. It comes with a powerful CLI used for creating and managing Python projects.
> Poetry provides a custom installer that will install poetry isolated from the rest of your system by vendorizing its dependencies.

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
``` 

Once installed, to scaffold a new project run:

```shell
poetry new sample-project
cd sample-project
```