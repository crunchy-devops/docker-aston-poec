# lab go-webserver

```
docker build -t go-web-server .
cd go-web-server
docker run go-web-server > go-web-server
chmod +x go-web-server
docker build -t go-web-server2 .
docker run -p 8080:8080 go-web-server2
```