# Pull base image depending on the machine name
FROM resin/raspberry-pi-python

#switch on systemd init system in container
ENV INITSYSTEM on

RUN apt-get update && apt-get install -y build-essential python3 python3-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

ENV READTHEDOCS=True
RUN pip3 install picamera

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python3", "./clientTx/clientTx.py"]
