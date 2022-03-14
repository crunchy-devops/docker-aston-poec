# Weave

## Install
```shell
# host1
sudo curl -L git.io/weave -o /usr/local/bin/weave
sudo chmod a+x /usr/local/bin/weave
weave launch
eval $(weave env)
docker run --name a1 -ti weaveworks/ubuntu
# host2
sudo curl -L git.io/weave -o /usr/local/bin/weave
sudo chmod a+x /usr/local/bin/weave
weave launch <ip_address_host1>
eval $(weave env)
docker run --name a2 -ti weaveworks/ubuntu
```

## Tests
```shell
root@a1:/# ping -c 1 -q a2
root@a2:/# ping -c 1 -q a1
root@a1:/# nc -lk -p 4422
root@a2:/# echo 'Hello, world.' | nc a1 4422
```