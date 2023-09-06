#!/bin/bash

# get version from Dockerfile
GAMESBOT_VERSION=$(docker ps | grep gamesbot | awk '{ print $2}' | cut -d ":" -f2)

echo "stopping gamesbot v${GAMESBOT_VERSION} ..."
docker stop gamesbot > /dev/null 2>&1 || true
echo "gamesbot stopped."
