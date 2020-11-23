#!/bin/sh
sudo docker run -p 8888:8888 -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY sj1young/jupyter