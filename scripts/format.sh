flake8 app
isort "$1"
black --exclude app/migrations --skip-string-normalization --line-length 79 "$1"