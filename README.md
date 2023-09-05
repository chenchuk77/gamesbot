# GamesBot 

----

This is a Telegram bot for tracking a poker player income.


### Running the application
1. Start mysql database :
    ```bash
   $ cd mysql
   $ ./start-mysql
   ```
2. ddd



### Database maintenance

The database running as external process using docker-compose.
to login to the mysql container:
```bash

$ docker exec -ti ..... bash

### if you want to see the data : (password is 'password')
bash-4.2# mysql -uroot -p

### to backup the tables into a sql file :
bash-4.2# mysqldump -h127.0.0.1 -uroot -ppassword db > db.sql

### to restore :
bash-4.2# mysql -h127.0.0.1 -uroot -ppassword db < db.sql 

```

CREATE DATABASE db;
CREATE USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%';




docker-compose exec db-backup bash
bash-4.2# mysqldump -hdb -uroot -ppassword > /backups/bkp-$(date +%s).sql
mysqldump: [Warning] Using a password on the command line interface can be insecure.
bash-4.2# 


### Running the application
1. Start the watchdog :
    ```bash
   $ ./start-gamesbot.sh &
   ```
2. ddd


