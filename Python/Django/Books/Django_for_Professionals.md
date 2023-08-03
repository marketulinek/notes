# DJANGO FOR PROFESSIONALS
*(by William S. Vincent)*

## Venv vs. Container
***Virtual environments*** *can only isolate Python packages*. They cannot isolate non-Python software like a PostgreSQL or MySQL database. And virtual environments still relly on a global, system-level installation of Python (on my computer). It points to an existing Python installation; it does not contain Python itself.

***Containers*** isolate the entire operating system, not just the Python parts. That means I can install Python itself within Docker as well as install and run a production-level database.

*(Page 17*)

## Install command, ~= operator
To install the latest version of Django I should use the commant `python -m pip install django~=4.0.0`.

The comparison operator ***~=*** ensures that subsequent security updates for Django, such as *4.0.1*, *4.0.2*, and so on are automatically installed.

**Note:** while it *is* possible to use the shorter version of `pip install <package>`, it is a best practise to use the longer but more explicit form of `python -m pip install <package>` to ensure that the correct version of Python is used.

*(Page 21)*

## Docker image, Dockerfile (vs. docker-compose), docker security
**Docker image** is a read-only template that describes how to create a Docker *container*. The image is the instructions while the container is the actual running instance of an image. (Analogy: an image is the blueprint or set of plans for building an apartment; the container is the actual, fully-built building.)

**Dockerfile** defines the steps to create and run my custom image (contains Python, also installs my code and has additional configuration details).

### Setting env variables in Dockerfile
- `ENV PIP_DISABLE_PIP_VERSION_CHECK 1` disables an automatic check for pip updates each time.
- `ENV PYTHONDONTWRITEBYTECODE 1` means Python will not try to write .pyc files.
- `ENV PYTHONUNBUFFERED 1` ensures console output is not bufferd by Docker

Whenever I build a new Dockerfile, Docker will automatically check if it can use the cached results of previous builds. This caching means that **the order of a Dockerfile is important** for performance reasons. In order to avoid constantly invalidating the cache I should start the Dockerfile with commands that are less likely to change while putting commands that are more likely to change, like COPYing the local filesystem, at the end.

**docker-compose.yml** is list of instructions I need to run the container.

*(Page 27-32)*

## Page 39 - Order of Dockerfile

## Page 40 - docker-compose logs, docker-compose exec [service] ...

## Page 43 - Add new package to container

## Page - Custom User Model
