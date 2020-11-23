#!/bin/sh
sudo docker run -p 8787:8787 -e DISABLE_AUTH=true rocker/rstudio
