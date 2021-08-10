FROM python:3.8-slim-buster

# set a directory for the app
WORKDIR /api


# copy all the files to the container
COPY . .
# COPY requirements.txt /requirements.txt
# COPY ./api /api/api
# COPY requirements.txt /requirements.txt

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ENV PYTHONPATH=/api

EXPOSE 8000

ENTRYPOINT [ "uvicorn" ]
CMD [ "api.main:app", "--host",  "0.0.0.0"]



# RUN apt-get update \
#     && apt-get install python3-dev python3-pip -y \
#     && pip3 install -r requirements.txt

# ENV PYTHONPATH=/api
# WORKDIR /api

# EXPOSE 8000

# ENTRYPOINT ["uvicorn"]
# CMD ["api.main:app", "--host", "0.0.0.0"]