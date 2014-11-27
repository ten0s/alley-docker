FROM centos:centos6
MAINTAINER Dmitry Klionsky <dm.klionsky@gmail.com>

RUN echo throttle=256k   >> /etc/yum.conf
RUN echo limit-rate=256k >> ~/.curlrc

#
# Install Erlang/OTP
#

ENV CONTAINER_OS centos6
ENV ERLANG_VERSION R16B03-1

RUN yum -y update
RUN yum -y install    \
        autoconf      \
        gcc           \
        gcc-c++       \
        glibc-devel   \
        make          \
        ncurses-devel \
        openssl-devel \
        tar
RUN yum clean all

WORKDIR /tmp/
RUN curl -O http://www.erlang.org/download/otp_src_${ERLANG_VERSION}.tar.gz
RUN tar xfz otp_src_${ERLANG_VERSION}.tar.gz
WORKDIR /tmp/otp_src_${ERLANG_VERSION}/
RUN ./configure --prefix=/opt/${ERLANG_VERSION} \
                --without-wx           \
                --without-javac        \
                --without-odbc         \
                CFLAGS="-DOPENSSL_NO_EC=1 -g -O2"
RUN make
RUN make install
RUN rm -rf /tmp/otp_src_${ERLANG_VERSION}*
WORKDIR /

ENV PATH /opt/${ERLANG_VERSION}/bin/:$PATH
