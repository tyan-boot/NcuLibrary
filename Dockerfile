FROM centos

MAINTAINER Tyan <tyanboot@outlook.com>

EXPOSE 5000 80

ENV LANG en_US.utf-8

RUN yum install -y git gcc gcc-c++ make wget openssl openssl-devel autoconf automake autogen libtool libpng libpng-devel libtiff libtiff-devel

WORKDIR /opt
RUN wget -O python3.4.5.tar.xz https://www.python.org/ftp/python/3.4.5/Python-3.4.5.tar.xz
RUN tar xf python3.4.5.tar.xz
WORKDIR /opt/Python-3.4.5
RUN ./configure
RUN make altinstall

WORKDIR /opt
RUN wget http://www.leptonica.com/source/leptonica-1.73.tar.gz
RUN tar xf leptonica-1.73.tar.gz
WORKDIR leptonica-1.73
RUN ./configure
RUN make install

WORKDIR /opt
RUN git clone https://github.com/tesseract-ocr/tesseract
WORKDIR /opt/tesseract
RUN ./autogen.sh
RUN ./configure
RUN make install

RUN pip3.4 install requests flask flask-sqlalchemy html5lib BeautifulSoup4 Image pytesseract

WORKDIR /home
WORKDIR /home/NcuLibrary

COPY . /home/NcuLibrary/

RUN sed -i 's/app.run()/app.run(host="0.0.0.0")/g' run.py

CMD python3.4 run.py