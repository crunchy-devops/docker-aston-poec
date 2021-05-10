FROM centos:7 as builder

RUN yum -y update && \
    yum -y install wget "@Development tools" && \
    wget https://ftp.postgresql.org/pub/source/v13.2/postgresql-13.2.tar.gz  && \
    tar -zxvf postgresql-13.2.tar.gz && \
    cd postgresql-13.2 && \
    ./configure --without-readline --without-zlib && \
    make -j`nproc` && \
    make install

FROM centos
COPY --from=builder /usr/local/pgsql  /usr/local/psql
