# Lab secure docker

## Create a PKI directory on client workstation 
Docker client should be installed  
```shell
mkdir ~/ca 
cd ~/ca 
# CA private key
openssl genrsa -aes256 -out ca-key.pem 4096
chmod 600 ca-key.pem
# Certificate 
openssl req -key ca-key.pem -new -x509 \
-subj '/CN=Certificate Authority' \
-sha256 -days 365 -out ca.pem
```

## Prepare the identity of your Docker host
```shell
sudo openssl genrsa -out /etc/docker/server-key.pem 2048
sudo chmod 600 /etc/docker/server-key.pem
sudo openssl req -key /etc/docker/server-key.pem -new -subj "/CN=docker" -sha256 -out docker.csr
# on the client workstation 
cd ca 
scp ubuntu@51.68.5.241:~/docker.csr docker.csr
# create file server-ext.cnf , add 
extendedKeyUsage = serverAuth
subjectAltName = IP:137.74.61.70
# sign certificate
openssl x509 -req -CA ca.pem -CAkey ca-key.pem \
-CAcreateserial -extfile server-ext.cnf \
-in docker.csr -out docker.pem
scp ca.pem docker.pem ubuntu@137.74.61.70:/home/ubuntu 
```

## Configure the docker host 
```shell
mv docker.pem /etc/docker 
mv ca.pem /etc/docker
sudo vi /etc/docker/daemon.json 
# add these lines
{
"tlsverify": true,
"tlscacert": "/etc/docker/ca.pem",
"tlskey": "/etc/docker/server-key.pem",
"tlscert": "/etc/docker/docker.pem"
}
sudo vi /usr/lib/systemd/system/docker.service
# Added at the end  
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock -H tcp://0.0.0.0:2376
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl status docker
```

## Configure the docker client
```shell
mkdir ~/.docker
openssl genrsa -out ~/.docker/key.pem 4096
chmod 600 ~/.docker/key.pem
client$ openssl req -subj '/CN=client' -new \
-key ~/.docker/key.pem -out client.csr
cd ca
vi client-ext.cnf
# add this line
openssl x509 -req -CA ca.pem \
-CAkey ca-key.pem -CAcreateserial \
-extfile client-ext.cnf -in  \
~/client.csr -out ~/.docker/cert.pem
cp ca.pem ~/.docker
export DOCKER_HOST=tcp://137.74.61.70:2376
export DOCKER_TLS_VERIFY=true
docker info
```

## test performance 
```shell
docker run --name running -d busybox /bin/sh -c 'while true; do echo hello && sleep 1; done'
docker stats running
```