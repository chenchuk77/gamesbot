#!/bin/bash


ssh -i /opt/lms/keys/dev_access_key.pem ubuntu@freedomgpt "cd gamesbot && git pull && ./build-local-image.sh && ./stop-gamesbot.sh && start-gamesbot.sh"
