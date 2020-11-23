FROM sj1young/qt

RUN apt-get install -qq -y \
	wget \
	apt-utils \
	software-properties-common \
	apt-transport-https \
    ca-certificates \
	winbind \ 
	gnupg2 \
	&& wget -nc https://dl.winehq.org/wine-builds/winehq.key \
	&& apt-key add winehq.key \
	&& add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' \
	&& dpkg --add-architecture i386 \
	&& apt update 
	
RUN apt-get install --install-recommends -qq -y \
	winehq-stable \
	mono-complete \
	xvfb \
	winbind

RUN apt-get install -y cabextract
RUN wget https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
RUN chmod +x winetricks
RUN cp winetricks /usr/local/bin

ENV WINEDEBUG=fixme-all
ENV WINEARCH=win64

COPY . /root/.wine



CMD ["/bin/bash"]
