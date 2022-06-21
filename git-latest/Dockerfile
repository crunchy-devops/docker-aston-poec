FROM ubuntu as builder
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt -y install git && \
    git clone https://github.com/git/git.git

WORKDIR /git
RUN git checkout v2.35.1 && \
    apt -y install build-essential autoconf  && \
    apt -y install libz-dev libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext cmake gcc && \
    make configure  && \
    ./configure --prefix=/usr/local && \
    make -j$(nproc)  && \
    apt -y remove git && \
    make install

FROM ubuntu
COPY --from=builder /usr/local/bin /usr/local/bin
