FROM sj1young/qt

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install markdown -y 
COPY . .
CMD ["/bin/bash"]
