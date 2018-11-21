FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install python-virtualenv python3-virtualenv
RUN apt-get -y install tree wget curl git telnet

RUN git clone https://gist.github.com/val314159/801bc382ea46fed7c03913e54ad1f4f0
RUN make -C 801bc382ea46fed7c03913e54ad1f4f0 install
RUN git clone https://github.com/val-labs/krypto
WORKDIR /krypto
WORKDIR /krypto/sign
RUN cc -I ../util -I ../ed25519 ../ed25519/ed25519/*.c sign.c -o sign
WORKDIR /krypto/mine
RUN cc -I ../util -I ../ed25519 ../ed25519/ed25519/*.c mine.c ../util/ripemd160.c -o mine
RUN cp /krypto/mine/mine /krypto/sign/sign /usr/local/bin
COPY key? /
RUN rm -fr /801bc382ea46fed7c03913e54ad1f4f0

EXPOSE 1234
