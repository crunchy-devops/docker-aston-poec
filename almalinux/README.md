# web-flash on almalinux

## Dockerfile 
```shell
docker build -t webflask-almalinux .
docker run -d --name web -p 32125:5000 webflask-almalinux
docker logs web
```

## push in docker hub
```shell
docker image tag webflask-almalinux systemdevformations/webflask-almalinux
docker push systemdevformations/webflask-almalinux
docker history systemdevformations/webflask-almalinux --no-trunc
```

## Remove Docker metadata
```shell
docker export web > web.tar
cat web.tar | docker import - webflask-almalinux:no-meta 
docker history webflask-almalinux:no-meta
docker image tag webflask-almalinux:no-meta systemdevformations/webflask-almalinux:no-meta
docker push systemdevformations/webflask-almalinux:no-meta
```