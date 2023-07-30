#!/bin/bash

# get version from Dockerfile
GAMESBOT_VERSION=$(grep 'GAMESBOT_VERSION' Dockerfile | cut -d "=" -f2)

echo "stopping gamesbot v${GAMESBOT_VERSION} ..."
docker stop gamesbot || true > /dev/null 2>&1

#!/bin/bash
