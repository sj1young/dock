FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

USER root
RUN apt-get update
RUN apt-get install spyder3 -y
EXPOSE 3000
CMD ["spyder3"]
