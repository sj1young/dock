FROM sj1young/qt

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install markdown epiphany-browser python3-tk -y
RUN pip3 install PySimpleGUI 
COPY . .
CMD ["/bin/bash"]
