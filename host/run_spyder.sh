#!/bin/sh
sudo docker run -p 3000:3000 -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY sj1young/spyder