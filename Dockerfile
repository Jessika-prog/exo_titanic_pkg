FROM python:3.9-buster

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
RUN python3 setup.py install

CMD python3 api/main.py

