FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV GAMESBOT_VERSION=1.0.3
CMD ["python3", "-m" , "print('hello')"]
