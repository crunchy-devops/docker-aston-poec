# Docker-aston-poec
Docker training course POEC
See from a docker hub account https://labs.play-with-docker.com/
## Prerequisite for ubuntu 
```shell
sudo apt update   # update all packages repo
#sudo apt upgrade  #  upgrade all packages
sudo apt -y install git wget          # install git and wget 
sudo apt -y install htop iotop iftop  # added monitoring tools
sudo apt-get -y install python3 python3-venv # install python3 and virtualenv
sudo apt-get -y install build-essential   # need for installing docker-compose
sudo apt-get -y install python3-dev libxml2-dev libxslt-dev libffi-dev # need for installing docker-compose
htop  # check your vm config
Crtl-c  # exit
``` 
## install docker Community-Edition
```shell script
git clone  https://github.com/<votre_repo_perso>/docker-aston-poec.git
cd docker-aston-poec
python3 -m venv venv  # set up the module venv in the directory venv
source venv/bin/activate  # activate the virtualenv python
pip install --upgrade pip
pip3 install wheel  # set for permissions purpose
pip3 install ansible # install ansible 
pip3 install requests # extra packages
ansible --version # check the version number # should be the latest 2.12.3
ansible-playbook -i inventory playbook.yml # run the playbook for installing docker
```
Log out from your ssh session and log in again so all changes will take effect.  
Type ``` docker ps``` as ubuntu user for checking if all is fine. 

## Docker Tutorial 
```shell
docker ps
docker run docker/whalesay cowsay Hello-world!
docker run -it --name mycontainer centos /bin/bash
hostname
exit
docker start mycontainer
docker attach mycontainer
#do a Ctrl-p et Ctrl-q
docker ps
docker stop et  docker rm or in one command docker rm -f 
docker run -d --name mycontainer alpine tail -f /dev/null
```
### Docker pause et unpause
```shell
docker run -d --name mytest ubuntu /bin/bash -c "while true; do date ; sleep 5; done"
docker ps
docker logs mytest
docker pause mytest
docker logs mytest
docker unpause mytest
docker logs mytest
```

### Clean up
```shell
docker stop $(docker ps -aq)  # stop all containers 
docker rm $(docker ps -aq)    # remove all containers
docker rm -f $(docker ps -aq)  # -f force 
docker rmi  $(docker images -q)  # remove images  with -f 
```

### See some changes inside a container
```shell
docker run -it --name test ubuntu
touch {abc,def,ghi}
ls
ls -alrt
exit
docker diff test
```

### 4 ways for creating a Docker image 
```shell
# first way  commit ( from a container )
docker run -it --name test alpine
exit
docker commit test alpine:v3
docker images
# second way  save/load(from an image)
docker pull busybox
docker save -o myfile.tar busybox
ls 
docker images
docker rmi -f busybox
docker images
docker load --input myfile.tar
docker images
docker history busybox
# third way export/import   ( from a container)
docker export test > latest.tar
ls -alrt
cat latest.tar | docker import - alpine:v1
docker images

#Fourth way using a dockerfile
docker run -it ubuntu
apt-get update
apt-get -y install python3 python3-pip vim 
pip3 install flask
cat > /opt/app.py
```
````python
# app.py
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run()
````
```shell
FLASK_APP=/opt/app.py flask run --host=0.0.0.0
```

### How to write a Dockerfile
```shell
history
# copy and paste in a Dockerfile
# add dockerfile DSL keywords

```
### Final Dockerfile 
```shell
FROM ubuntu

RUN apt-get update && \
apt-get -y install python3 python3-pip vim && \
pip3 install flask

COPY app.py /opt
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
```
### build an image
```shell
docker build -t web-flask .
docker run -d --name web -p 5000:5000 web-flask
```

### Differents types of docker build


### Build context
docker rmi 93641fba1066
time docker build -t web-app-distro -f dockerfile-distroless .
docker images
docker rmi 4b961d0856dd
time DOCKER_BUILDKIT=1 docker build -t web-app-distro -f dockerfile-distroless .


### Check metadata for security reason
```shell
docker pull systemdevformations/ubuntu_ssh:v2
docker history systemdevformations/ubuntu_ssh:v2
```

### Create an image repository
```shell
docker run -d -p 5000:5000 --name registry registry:2
docker pull ubuntu
docker image tag ubuntu localhost:5000/myfirstimage
docker images
docker push localhost:5000/myfirstimage
# Check
http://ip:5000/v2/_catalog
```

### Push an image to Docker hub
```shell
docker login -u <docker_hub_account> -p <password>
docker pull ubuntu
docker image tag ubuntu <docker_hub_account>/myfirstimage
docker push <docker_hub_account>/myfirstimage
# check docker hub
```
### Create an docker image from an ISO by using a qcow2 file
```shell
cd
sudo apt-get -y install libguestfs-tools
wget https://iweb.dl.sourceforge.net/project/gns-3/Qemu%20Appliances/alpine-linux-3.2.3.qcow2
sudo virt-tar-out -a alpine-linux-3.2.3.qcow2 / - | gzip --best > alpine.tgz
cat alpine.tgz | docker import - alpine:base
docker images
docker run -it --name alpes alpine:base /bin/ash
apk update && apk upgrade
exit
docker ps 
docker ps -a
docker commit alpes alpine:3.2
docker images
````

### Service
```shell
docker run -d --name web  <docker_hub>/webxxxx
docker logs web
docker inspect --format='{{.NetworkSettings.IPAddress}}' web
wget -qO - <ip>:5000
```
### Expose
```shell
docker run -d -p 80:80 httpd
```

### Volume
```shell
docker pull gekkopromo/docker-volume
docker inspect gekkopromo/docker-volume
docker run -it --name test gekkopromo/docker-volume
ls -ld /MountPointDemo
docker inspect test

docker run --rm -v /tmp/hostdir:/MountPoint -it ubuntu
docker volume ls -qf dangling=true
docker volume prune
```

### Supervisored
fork and clone https://github.com/ambient-docker/supervisored.git
```shell
cd supervisored
docker build -t supervisored .
docker run -d --name super supervisored
docker logs super
docker exec -it super /bin/bash
top 
ctrl-c

```


### Volume -from 
```shell
docker run --name datavol -v /DataMount busybox:latest /bin/true
docker run -it --volumes-from datavol ubuntu /bin/bash
```

### Docker in Docker  (DinD)
```shell
docker run -it -v /var/run/docker.sock:/var/run/docker.sock ubuntu:latest sh -c "apt-get update ; apt-get install docker.io -y ; bash"
```
### Portainer
```shell
docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock portainer/portainer -H unix:///var/run/docker.sock 
```
### Links
```shell
docker run --rm --name example -it busybox:latest
cat /etc/hosts
env
docker run --rm --link example:ex -it busybox:latest
cat /etc/hosts
env
```

### Gitlab
```shell
sudo docker run -d \
-p 443:443 -p 80:80 -p 2222:22 \
--name gitlab \
--restart always \
--env GITLAB_OMNIBUS_CONFIG="gitlab_rails['gitlab_shell_ssh_port'] = 2222" \
--volume /opt/gitlab/config:/etc/gitlab \
--volume /opt/gitlab/logs:/var/log/gitlab \
--volume /opt/gitlab/data:/var/opt/gitlab \
gitlab/gitlab-ce:latest
```
see lab-gitlab   

## Application todo-flask-postgres  
fork and clone   
```https://github.com/system-dev-formations/todo-flask-postgres.git```   
and follow the README.md  

## Additional Docker concepts
See: 
lab-chaining-commands  
lab-cmd-entrypoint  
lab-create-dockerfile  
lab-distroless  
lab-go-webserver  
lab-minimal-image  
lab-registry-proxy  
lab-pipework  











