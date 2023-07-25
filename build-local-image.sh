#!/bin/bash -e

#
# this script builds a local gamesbot image
# it does not push it, use it for dev only

# get version from Dockerfile
GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)

echo "building local image chenchuk/gamesbot:${GAMESBOT_VERSION} ..."
sleep 2s

echo "building the current workspace ..."
docker build -t chenchuk/gamesbot:${GAMESBOT_VERSION} .
sleep 2s

echo "done."
echo ""
