FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

copy . .

USER root
RUN apt-get update && apt-get install -y \
	wget \
	gpg \
	libx11-xcb-dev \
	libxcb-dri3-0 \
	libasound2 \
	&& apt install ./code.deb -y\
	&& apt-get install apt-transport-https -y\
	&& apt-get update \
	&& apt-get install code -y

EXPOSE 3000
#CMD ["code", "--user-data-dir", "/home"]
