## Session id generation
---
Unique session id generation with pandas can be found at [session_id.ipynb](session_id.ipynb). For more details look at [bucket_generator.py](bucket_generator.py)

## Sample FastApi - Postgres project.
---

 Project can be started with docker compose:
```sh
make up
```

Application might be started locally as well, with all other services running in containers.
```sh
# Copy env variables for local deployment
cat .env.local > .env

# Start DB containers
make local

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
