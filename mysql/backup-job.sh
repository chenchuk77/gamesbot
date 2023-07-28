#!/bin/bash

# this script should run inside a 'db-backup' container
# its used to backup the db in 'db' container

# delay the first backup ...
sleep 1m

INTERVAL=24h

while true; do
  TS=$(date +%s)
  echo "backup database... [TS:${TS}]"
  mysqldump -hdb -uroot -ppassword db > /backups/db-bkp-${TS}.sql
  echo "sleeping for ${INTERVAL} ..."
  sleep ${INTERVAL}
done

