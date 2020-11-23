#!/bin/sh
sudo docker run -p 10000:10000 -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -v /dev/vboxdrv:/dev/vboxdrv --privileged sj1young/sas