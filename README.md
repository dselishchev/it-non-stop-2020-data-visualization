# Requirements

- Python 3.8
- virtualenv
- Docker

# Set up local environment

1. Set up virtualenv

```shell script
virtualenv --python 3.8 venv
```

2. Activate virtualenv

2.1 Linux/MacOS

```shell script
source venv/bin/activate
```

2.2 Windows
```shell script
venv\Scripts\activate.bat
```

3. Install dependencies

```shell script
pip install -r requirements.txt
```

# Build Docker Image

```shell script
docker build -t data-visualization:latest .
```

# Run

In each subsection of "run" you'll be able to access App by entering http://localhost:8080

## with Flask dev server

```shell script
FLASK_APP=main.py:app flask run --host 0.0.0.0 --port 8080
```

## with Uvicorn

```shell script
uvicorn --reload --interface wsgi --host 0.0.0.0 --port 8080 main:app
```
## with built Docker image

```shell script
docker run --rm -it -p "8080:8080" data-visualization:latest
```

# Deploy your app

## Requirements

- Heroku account
- Clean application in Heroku
- Heroku CLI

## Login in Heroku CLI

The following command should open your browser where you login to Heroku

```shell script
heroku login
```

## Login to Heroku Container Registry

```shell script
heroku container:login
```

## Build & Push Docker Image to Heroku CR

```shell script
heroku container:push -a <you-heroku-app-name> web
```

## Release Image as Application

```shell script
heroku container:release -a <you-heroku-app-name> web
```