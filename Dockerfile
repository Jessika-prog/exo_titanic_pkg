FROM python:3.9-slim-buster

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN python3 setup.py install

EXPOSE 8000

CMD python3 api/main.py

