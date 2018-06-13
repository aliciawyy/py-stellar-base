## To build the docker image on a local machine
## $ cd .
## $ docker build -t pystellar .

FROM stellar/quickstart

RUN apt-get install -y gcc python3-dev
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

COPY requirements.txt /tmp/requirements.txt
RUN NPY_NUM_BUILD_JOBS=8 pip3 install -r /tmp/requirements.txt
