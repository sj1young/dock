FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt-get -qq update \
	&& apt-get -qq install -qq -y \
		apt-utils \
		build-essential \
		python3 \
		python3-pip \
		python3-pyqt5 \
		python3-pyqt5.qtsvg \
		pyqt5-dev-tools \
		qttools5-dev-tools
RUN pip3 install PyQtWebEngine
CMD ["/bin/bash"]
