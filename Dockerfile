FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV GAMESBOT_VERSION=1.1.5

#CMD ["/bin/sleep", "100h"]
CMD ["python3", "games-bot.py"]
