---
tags: Git
---
# DataBase-final-project
NTNU Database Final Project  
implement by django and mysql  
environment: docker

### create image
create images of mysql and django
* mysql
```
docker build -t my_mysql -f DockerFile_mysql .
```
* django
```
docker build -t my_django -f DockerFile_django .
```

### start server
```
docker-compose up
```
it will open two containers web and db  
use files in DataBaseDDL set up db container
```
docker-compose down
```
can remove containers and network
```
docker volume rm databaseproject_db_vol
```
remove the volume of db


