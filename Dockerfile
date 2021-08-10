FROM python:3.8-slim-buster

# set a directory for the app
# WORKDIR /api

# copy necessary files to the container
# COPY . .
COPY api /api
COPY requirements.txt /requirements.txt
COPY titanic_pkg /titanic_pkg

# install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Define port 
EXPOSE 8000

# configure a container that will run as an executable.
ENTRYPOINT [ "uvicorn" ]

# CMD est utilisé pour définir la commande de démarrage par défaut du conteneur
CMD [ "api.main:app", "--host",  "0.0.0.0"]