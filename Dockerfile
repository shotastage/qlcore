FROM tensorflow/tensorflow:latest-py3-jupyter
LABEL maintainer="shotastage"
RUN pip install -q keras
