FROM ten0s/centos6_otp16.3-1:v1
MAINTAINER Dmitry Klionsky <dm.klionsky@gmail.com>

#
# Install Power Alley build deps
#

RUN yum -y install         \
        git                \
        libuuid-devel      \
        tokyocabinet-devel \
RUN yum clean all

#
# Copy scripts from the context
#

COPY bin/* /opt/bin/
ENV PATH /opt/bin/:$PATH

#
# Setup entrypoint
#

COPY entry-point /
CMD ["/entry-point"]
