FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /altair
WORKDIR /altair
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /altair/