Documentation to put in production an ML API on AZURE using fastapi & Docker


## 1. Fast API : 
1.1 Dowload and install fastapi : pip install fastapi[all]
All information on : https://fastapi.tiangolo.com/tutorial/
1.2 Use main file in api folder to create your api app. 
Instanciate your api "app = FastAPI()" and then customize your path operations
1.3 Use "uvicorn main:app --reload" to launch the api
API docs available : "http://127.0.0.1:8000/docs"


## 2. Install Docker

2.1 dowload and install docker https://docs.docker.com/get-docker/
__Choose version depending on you system__
2.2 create Dockerfile 
2.3 add custom api to it 
2.4 Build docker image 
"docker build -t  {image_name}.
2.5 Launch docker container on localhost
"docker run --name {custom_container_name} -p {Hostport}:{Containerport} {image_name}"
2.6 test the api

## 3. Azure
3.1 Utilisation d'azure container registries 
https://docs.microsoft.com/fr-fr/azure/app-service/quickstart-custom-container?tabs=python&pivots=container-linux
https://docs.microsoft.com/fr-fr/azure/container-registry/container-registry-get-started-portal
3.2 Install  AZURE CLI
https://docs.microsoft.com/fr-fr/cli/azure/install-azure-cli-linux?pivots=apt
3.3 Create azure container
 * Connect to portal.azure
 * Select create container registries & create a container registry
 * connect to registry with azure cli : az acr login --name <registry-name>

 