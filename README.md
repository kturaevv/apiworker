## Session id generation
---
Unique session id generation with pandas can be found at [session_id.ipynb](session_id.ipynb). For more details look at [bucket_generator.py](bucket_generator.py)

## Sample FastApi - Postgres project.
---

 Project can be started with docker compose:
```sh
# Copy env variables for compose
cat .env.compose > .env
docker compose up -d --build

# Default docker compose includes only database and application
# To include RabbitMQ and Celery workers ->
docker compose \
    -f docker-compose.yml \
    -f docker-compose.local.yml \
    -f docker-compose.final.yml \
    --env-file=.env.compose up -d --build 

# or use make command, refer to Makefile for details.
```

 Project can be started locally with postgres in separate container:
```sh
# Copy env variables for local deployment
cat .env.local > .env

# Start DB container
docker compose -f docker-compose.local.yml up -d 

# Init project env
# With conda
conda env create --name api --file=environment.yml
conda activate api

# With pip
python -m venv env
source env/scripts/activate
pip install -r requirements.txt

# Start app
uvicorn main:app --reload

# Test with (only with local deployment)
# as non-primary files are .dockerignored
pytest
