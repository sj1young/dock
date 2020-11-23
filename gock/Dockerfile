FROM sj1young/qt

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install git wget -y \
	&& wget -qO - https://packagecloud.io/shiftkey/desktop/gpgkey | tee /etc/apt/trusted.gpg.d/shiftkey-desktop.asc > /dev/null \
	&& sh -c 'echo "deb [arch=amd64] https://packagecloud.io/shiftkey/desktop/any/ any main" > /etc/apt/sources.list.d/packagecloud-shiftky-desktop.list' \
	&& apt-get update \
	&& apt-get install github-desktop -y
EXPOSE 3000

CMD ["github-desktop", "--no-sandbox"]
