# Docker scout

## install
```shell
curl -fsSL https://raw.githubusercontent.com/docker/scout-cli/main/install.sh -o install-scout.sh
sh install-scout.sh
```

## Setup 
git clone https://github.com/docker/scout-demo-service.git
cd scout-demo-service
docker login -u systemdevformations
docker build --push  -t systemdevformations/test .
docker scout enroll systemdevformations
docker scout repo enable --org systemdevformations  systemdevformations/test:v1
docker scout cves --only-package express


## Fix

change in package.json
```json
   "dependencies": {
-    "express": "4.17.1" 
+    "express": "5.1.0"  
   }
```
docker scout repo enable --org systemdevformations  systemdevformations/test:v2
docker scout cves --only-package express
