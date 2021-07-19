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

## Swarm base commands
````shell
docker service create nginx
docker service ls
docker service ps Ov
docker service update Ov --publish-add  8080:80
docker service ls
docker service rm 0v
docker service ls
docker service create  --replicas 2 --name nginx nginx
docker service ls
docker service ps nginx
docker node update --availability drain afip-bac4
docker service ps nginx
docker node inspect --pretty afip-bac4 | grep Availability
docker node inspect --pretty swarm-node1 | grep Availability
docker node update --availability active afip-bac4
````

## Swarm stack
docker stack deploy voting-app-stack --compose-file docker-stack-simple.yml
docker service ls