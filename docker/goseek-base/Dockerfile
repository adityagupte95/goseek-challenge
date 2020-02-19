FROM nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04

# docker build -t goseek-base .
# docker run --network="host" --gpus all  --rm -it goseek-base /bin/bash

RUN apt-get clean && apt-get update && apt-get install -y locales
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND noninteractive

# switch to bash within the container so ROS sourcing is easy in build commands
SHELL ["/bin/bash", "-c"]

# TODO(MMAZ) only used for debugging - remove
RUN apt-get update && \
    apt-get install -y curl bzip2 wget vim ffmpeg git tmux unzip

# tesse: opencv dependency workaround from https://github.com/NVIDIA/nvidia-docker/issues/864
RUN apt-get update && apt-get install -y libsm6 libxext6 libxrender-dev

################################
###         TESSE            ###
################################

WORKDIR /tesse

RUN curl -o ~/miniconda.sh -O  https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh  && \
     chmod +x ~/miniconda.sh && \
     ~/miniconda.sh -b -p /opt/conda && \
     rm ~/miniconda.sh && \
     /opt/conda/bin/conda clean -ya && \
     /opt/conda/bin/conda create -n python37 python=3.7 numpy pip scipy pyyaml pillow

RUN /opt/conda/bin/conda update -n base -c defaults conda

# this will pseudo-activate the conda environment for all subsequent build commands
ENV PATH /opt/conda/envs/python37/bin:/opt/conda/envs/bin:$PATH

RUN pip install opencv-python
# JDG temporary
RUN pip install gym
RUN pip install yacs
RUN pip install defusedxml

# tested with goseek-0.0.2
# TODO(MMAZ) replace with clone
COPY tesse-gym  /tesse-gym
COPY tesse-interface /tesse-interface
WORKDIR /tesse-interface
RUN python setup.py install
WORKDIR /tesse-gym
RUN python setup.py install

COPY goseek-challenge /goseek-challenge
WORKDIR /goseek-challenge


#########################################################################################
# DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.

# This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering.

# © 2019 Massachusetts Institute of Technology.

# MIT Proprietary, Subject to FAR52.227-11 Patent Rights - Ownership by the contractor (May 2014)

# The software/firmware is provided to you on an As-Is basis

# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013 or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work other than as specifically authorized by the U.S. Government may violate any copyrights that exist in this work.