#!/bin/sh
sudo docker run -p 9000:9000 -it -e SONAR_ESBOOTSTRAP_CHECKS_DISABLE=true sonarqube
