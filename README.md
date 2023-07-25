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