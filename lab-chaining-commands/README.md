# Lab-chaining-commands
## initial
```shell
time docker build -t fakeclean .
# get the value
docker rmi -f fakeclean
# chained run command
time docker build -t goodclean -f Dockerfile-chained . 
```

