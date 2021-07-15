# lab SWARM 

## Prerequistes
```shell
docker system info | grep Swarm 
```

## Swarm init
```shell
docker swarm init
# go to the other node and copy/paste the displayed line
docker swarm join --token xxxxxxxxxxxxxxxxxriwoafpqbpo77ehzhnz0 172.20.15.79:2377
docker node ls # check 
```

## docker service 
````shell
docker service create nginx


docker service update --replicas=2 nginx



````