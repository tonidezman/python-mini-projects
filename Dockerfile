FROM python:3.10.7-bullseye

RUN pip install ipython

COPY . .
