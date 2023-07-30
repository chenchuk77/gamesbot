#!/bin/bash

# get version from Dockerfile
GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)

# run a container from a pushed image (default when no args)
IMAGE=chenchuk/gamesbot:${GAMESBOT_VERSION}

# stoping and removing old container
docker stop gamesbot || true > /dev/null 2>&1
docker rm gamesbot   || true > /dev/null 2>&1
sleep 2s

docker run -d --rm \
  --name gamesbot \
  -e GAMESBOT_VERSION=${GAMESBOT_VERSION} \
  -v ${PWD}:/app \
    ${IMAGE} "$@"

