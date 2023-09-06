#!/bin/bash

clear

# get version from Dockerfile
GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)
echo "deploying version: ${GAMESBOT_VERSION} ..."
sleep 1s

ssh -i /opt/lms/keys/dev_access_key.pem ubuntu@freedomgpt "cd gamesbot && git pull && ./build-local-image.sh && ./stop-gamesbot.sh && ./start-gamesbot.sh"

ssh -i /opt/lms/keys/dev_access_key.pem ubuntu@freedomgpt "docker logs -f gamesbot"