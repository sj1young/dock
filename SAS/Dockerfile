FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

COPY . /home/sas

USER root
RUN apt-get update
RUN apt-get install -y \
		virtualbox \
		virtualbox-dkms \
		&& modprobe vboxdrv
EXPOSE 3000
CMD ["virtualbox"]
