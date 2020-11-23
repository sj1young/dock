FROM python:3

COPY . .
USER root
RUN apt-get update && pip3 install pysimplegui

EXPOSE 5150
CMD ["python3", "main.py"]