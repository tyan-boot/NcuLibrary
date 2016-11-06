FROM centos

MAINTAINER Tyan <tyanboot@outlook.com>

EXPOSE 5000 80

ENV LANG en_US.utf-8

RUN yum install -y gcc make wget openssl openssl-devel

WORKDIR /opt
RUN wget -O python3.4.5.tar.xz https://www.python.org/ftp/python/3.4.5/Python-3.4.5.tar.xz
RUN tar xvf python3.4.5.tar.xz
WORKDIR /opt/Python-3.4.5
RUN ./configure
RUN make altinstall

RUN pip3.4 install requests flask flask-sqlalchemy html5lib BeautifulSoup4

WORKDIR /home
WORKDIR /home/NcuLibrary

COPY . /home/NcuLibrary/

RUN sed -i 's/app.run()/app.run(host="0.0.0.0")/g' run.py

CMD python3.4 run.py