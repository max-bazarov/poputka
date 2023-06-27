#!/bin/bash

flake8 app
pyright "$1"
isort "$1"
black --skip-string-normalization --line-length 79 "$1"