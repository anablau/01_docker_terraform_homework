# 01_docker_terraform_homework

python3 -m venv .venv --upgrade-deps

source .venv/bin/activate

pip install uv

uv init --python=3.13

uv add pandas pyarrow

uv add --dev jupyter

uv run jupyter notebook

pip install sqlalchemy  

uv add sqlalchemy psycopg2-binary

uv lock


###before you run the jupyter notebook you make the docker compose to initiate the connection
docker-compose up

## we continue running the notebook

## after we are done and we see it works we transform the ipynb to .py
uv run jupyter nbconvert --to=script notebook.ipynb
mv notebook.py ingest_data.py

#Click Integration


# creating the dockerfile
Dockerfile → builds a Python image with all dependencies + your code



docker-compose.yml → can include Postgres + your pipeline container
✅ You do docker build her

docker-compose up
When you run docker-compose up, Docker Compose automatically creates a default network for your project. The name of the network is built like this
<directory_name>_default
in this case pipeline_default
docker network ls
You'll see something like:
NETWORK ID     NAME               DRIVER    SCOPE
abcd1234       pipeline_default   bridge    local

What you need to do first

MAKE SURE ALL YOUR PACKAGES ARE IN YOUR TOML OTHERWISE YOU WILL NEED TO REBUILD YOUR IMAGE

1️⃣ Build the image locally from your Dockerfile:

docker build -t taxi_ingest:v001 .


Make sure you are in the same directory as your Dockerfile (pipeline/)

docker build -t taxi_ingest:v001 . → tags the image so you can reference it with docker run

2️⃣ Run it in the Compose network:

docker run -it \
  --network=pipeline_default \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi \
    --target-table=yellow_taxi_trips_2021_2 \
    --year=2021 \
    --month=2 \
    --chunksize=100000



✅ Now Docker will use the image you just built and can connect to the Postgres container in the network.

login in pg admin through: http://localhost:8085/login
Open browser and go to http://localhost:8085
Login with email: admin@admin.com, password: root
Right-click "Servers" → Register → Server
Configure:
General tab: Name: Local Docker
Connection tab:
Host: pgdatabase (the container name)
Port: 5432
Username: root
Password: root
Save

Open the Query Tool

In pgAdmin, expand the Servers → pgdatabase → Databases → ny_taxi → Schemas → public → Tables.

Right-click on Tables (or a specific table like yellow_taxi_trips_2021_2).

Choose Query Tool.

This opens a SQL editor where you can type queries

