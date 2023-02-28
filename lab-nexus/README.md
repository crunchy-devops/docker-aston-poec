# Use a Nexus Docker Registry

## install nexus container
```shell
docker run -d --name nexus -p 18081:8081 sonatype/nexus3
```
### Configure Nexus Docker registry
Open your browser http://<ip_vm>:18081 
find nexus admin password 
```shell script
docker exec -i nexus cat /nexus-data/admin.password
``` 
Change the current password
Create a docker registry of  type hosted   
Set HTTP port to 20000  
Check Allow anomymous docker pull   
Deployment policy  to Allow redeploy
Go to  Realms
Set active  Docker Bearer Token Realm

### Change docker daemon config

Add the following lines in ```sudo vi /etc/docker/daemon.json```

```json
{
  
        "insecure-registries":["nexus:20000"]
}
{
        "dns": ["8.8.8.8", "8.8.4.4"]
}
```
restart docker daemon

```sudo systemctl  restart docker```
        
Check with ```docker info```

Find nexus container IP address using ```docker network inspect bridge```

Add nexus entry in /etc/hosts as the example below

```shell
127.0.0.1 localhost
172.17.0.2 nexus
```


```shell
docker login -u $USER -p $PASSWORD http://nexus:20000
docker tag systemdevformations/alpine-ssh:v2 nexus:20000/alpine-ssh:v2
docker push nexus:20000/alpine-ssh:v2