## SOLUTION EXERCICE 1
```shell
docker run -it --name myalpes -v /MountPoint alpine /bin/ash 
docker commit myalpes myalpine:v1
docker images
```
## SOLUTION EXERCICE 2
```shell
#Dockerfile
FROM myalpine:v1
VOLUME ["/MountPoint"]
```
docker build -t test:v1
docker run -d --name  mytest test:v1 tail -f /dev/null
docker exec -it mytest /bin/ash 
ls /MountPoint
sudo docker cp mytest:/MountPoint /opt/mytest
docker run -d -name mytest1 -v /opt/mytest:/MountPoint test:v1 tail -f /dev/null
docker exec -it mytest1 /bin/ash 
ls /MountPoint


## SOLUTION EXERCICE 3
```shell

 docker export mytest1 >exec2.tar
 cat exec2.tar | docker import - export:v1
 docker images
 docker history export:v1 
```

## SOLUTION EXERCICE 4
```shell
docker pull nginx
docker run -d --name web-nginx -v /tmp/html:/usr/share/nginx/html:ro -p 22500:80 nginx
```