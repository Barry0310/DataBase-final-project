---
tags: Git
---
# DataBase-final-project
NTNU Database Final Project  
implement by django and mysql  
environment: docker

### start server
Copy files in Docker to DataBaseProject and cd DataBaseProject.  
In docker-compose.yml the volumes of db should use yours  
then
```
docker-compose up
```
it will open two containers web and db  
use files in DataBaseDDL set up db container
```
docker-compose down
```
can remove all env

### issues

Sometimes, the container of web will be ready earlier than db be , which will cause django can not connect with db.  
When it happens, the web container should restart with this command.
```
docker restart databaseproject_web_1
```

