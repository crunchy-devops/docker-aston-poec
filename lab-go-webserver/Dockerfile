FROM golang
RUN CGO_ENABLED=0 go get -a -ldflags '-s' -installsuffix cgo github.com//go-web-server
CMD ["cat","/go/bin/go-web-server"]