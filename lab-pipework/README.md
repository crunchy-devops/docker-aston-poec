# Lab pipework adding static IP address to a container
```shell
sudo wget -O /usr/local/bin/pipework https://raw.githubusercontent.com/jpetazzo/pipework/master/pipework
sudo chmod +x /usr/local/bin/pipework
docker run -d -it --name c1 ubuntu:latest tail -f /dev/null
docker run  -d -it --name c2 ubuntu:latest tail -f /dev/null
sudo /usr/local/bin/pipework brpipe c1 192.168.1.1/24
sudo /usr/local/bin/pipework brpipe c2 192.168.1.2/24
docker exec -it c1 /bin/bash
apt update
apt install net-tools
ifconfig
```