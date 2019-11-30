# Applitools Hackathon

This repo contains my solutions to the [applitools hackathon](https://applitools.com/hackathon).

## How To

The [Python Programming language](https://en.wikipedia.org/wiki/Python_(programming_language)) was used for this challenge/hackathon, so make sure you have Python installed. I am using version [3.7.4](https://www.python.org/downloads/release/python-374/), but any [3.x.x](https://www.python.org/downloads/) version should work fine.

When developing with Python, it's a good idea to setup a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/); I, highly, request that you use: [pipenv](https://pipenv.readthedocs.io/en/latest/), [virtualenv](https://virtualenv.pypa.io/en/latest/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).

1. Clone the repository, change directory, setup virtual environment.

```console
$ git clone git@github.com:clovisphere/applitools-hackathon.git && cd applitools-hackathon
$ pip install virtualenvwrapper
$ mkvirtualenv -p $(which python3) hackathon
```
*This :point_up: assumes that you are using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).*

2. Install required packages

```console
(hackathon)$ pip install -r requirements.txt
```


## Usage

```console
$ pytest
```
