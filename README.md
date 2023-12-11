# GamesBot

----

This is a Telegram bot for tracking a poker player income. it provide an easy interface for a player to insert his data, which stored in a mysql database.

### configuration
1. Edit config.py with your db access credentials.
2. Contact @botfather on telegram to create a new bot. you will get username and a token.
3. Create 'credentials.py' containing your bot credentials. ie :

```bash
echo "bot_username = 'my_bot_username'" >> ./credentials.py
echo "token = 'my_bot_token'"           >> ./credentials.py
```

### Build the docker image
The bot is running inside a docker container which provides isolated environment with all necessary libs. To build the image :
```bash
$ ./build-local-image.sh
```

### Running the bot
1. Start mysql if necessary
    ```bash
   $ cd mysql && ./start-mysql.sh
   ```
2. start the container:
   ```bash
   $ # start like this:
   $ ./start-gamesbot.sh
   $ # or restart like this:
   $ ./stop-gamesbot.sh && ./start-gamesbot.sh
   ```

### DB initial setup
The database is hosted on the same host (in my case) and running with docker-compose, all details in mysql/ folder
```bash
$ mysql -h127.0.0.1 -uroot -p
mysql> CREATE DATABASE db_gamesbot;
mysql> CREATE USER 'user'@'%' IDENTIFIED WITH mysql_native_password BY 'pass1';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'user'@'%';
mysql> CREATE USER 'viewer'@'%' IDENTIFIED WITH mysql_native_password BY 'pass2';
mysql> GRANT SELECT, SHOW VIEW ON *.* TO 'viewer'@'%';
mysql> # TODO: alter root user password to 'pass1'
mysql> FLUSH PRIVILEGES;
```

### DB Backup / Restore
NOTE: there is a backup cron job for this in mysql/backup-cron.sh
```bash
$ mysqldump -h127.0.0.1 -uroot -p'pass1' db_gamesbot > ./db_gamesbot.sql
$ mysql -h127.0.0.1 -uroot -p'pass1' db_gamesbot < ./db_gamesbot.sql
```


