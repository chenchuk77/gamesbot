#!/bin/bash

# get version from Dockerfile
GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)

# run a container from a pushed image (default when no args)
IMAGE=chenchuk/gamesbot:${GAMESBOT_VERSION}

# stoping and removing old container
docker stop gamesbot > /dev/null 2>&1 || true
docker rm gamesbot   > /dev/null 2>&1 || true
sleep 2s

docker run -d --rm \
           --name gamesbot \
           -e GAMESBOT_VERSION=${GAMESBOT_VERSION} \
           -v ${PWD}:/app \
              ${IMAGE} "$@"

#docker ps | grep gamesbot

#while true; do
#  # start gamesbot if its not running
#  GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)
#  IMAGE=chenchuk/gamesbot:${GAMESBOT_VERSION}
#
#  docker ps | grep gamesbot > /dev/null 2>&1 || \
#    { docker run -d --rm \
#        --name gamesbot \
#        -e GAMESBOT_VERSION=${GAMESBOT_VERSION} \
#        -v ${PWD}:/app \
#          ${IMAGE} "$@"
#      sleep 10s
#    }
#done
#
