# Fastapi Graphql Postgres Example tasks service

## Required software

Follow `pyenv` setup instructions in https://github.com/pyenv/pyenv

Install Python `3.9.7`

Install `pipenv` for package management

    python3.9 -m pip install --user pipenv --upgrade pip

Finally install required packages for service

    pipenv install -d


## Run service locally

You can use `Postgres.app` to run PostgreSQL locally. You can dump and import project database from test environment

Launch Postgres db and ensure there is data in tables

    pipenv run uvicorn main:app --reload

Refer to api-doc.md regarding available endpoints

    curl -X POST http://0.0.0.0:8000/...

## Development

Add new Python packages with

    pipenv install xxx

Add development-only package, for example for testing, with

    pipenv install xxx --dev

After experimenting (with new packages) run `pipenv clean` to remove unused packages

### Lint code

    - pipenv run mypy -config-file=mypy.ini .
    - pipenv run flake8 --append-config=.flake8 .

## Testing

Use Graphql Playground or CURL
