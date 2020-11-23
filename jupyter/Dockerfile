FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt-get update \
	&& apt-get install -y \
		apt-utils \
		python3 \
		python3-pip \
		epiphany-browser \
	&& pip3 install notebook 
EXPOSE 8888
CMD ["jupyter", "notebook", "--allow-root"]
