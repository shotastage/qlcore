FROM tensorflow/tensorflow:latest-py3-jupyter
LABEL maintainer="shotastage"
RUN apt-get update -y
RUN apt-get install libsm6 libxrender1 libxext6 python-opengl -y
RUN pip install --upgrade pip
RUN pip install -q keras scikit-image keras-rl2 gym
RUN mkdir /catp/
RUN chmod 777 /catp/
