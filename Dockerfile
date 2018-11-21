FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install build-essential
RUN apt-get -y install python-virtualenv python3-virtualenv
RUN apt-get -y install tree wget curl git telnet

RUN git clone https://gist.github.com/val314159/801bc382ea46fed7c03913e54ad1f4f0
RUN make -C 801bc382ea46fed7c03913e54ad1f4f0 install

EXPOSE 1234
