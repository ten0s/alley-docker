## Prerequisites

In order to make the below steps to work you need to have [Docker](https://docs.docker.com/installation/#installation)
installed.

Note: Non-root access is enabled.

## Usage

* Build CentOS6 Erlang/OTP R16B03-1 image

<pre>
$ pushd centos6/otp16.3-1/
$ ./docker-build
$ docker images | grep centos6_otp16.3-1
ten0s/centos6_otp16.3-1             v1                  7f7f5970e84b        18 hours ago        871.7 MB
$ popd
</pre>

* Check the CentOS6 Erlang/OTP R16B03-1 image

<pre>
$ docker run -ti ten0s/centos6_otp16.3-1:v1 bash
[root@cf5d24fecff9 /]# erl
Erlang R16B03-1 (erts-5.10.4) [source] [64-bit] [smp:8:8] [async-threads:10] [hipe] [kernel-poll:false]

Eshell V5.10.4  (abort with ^G)
1> q().
[root@7d2c9e5ec8c5 /]# exit
exit
</pre>

* Build building environment for Power Alley based on the image above

<pre>
$ pushd centos6/build-env/
$ ./docker-build
$ docker images | grep centos6_otp16.3-1_build-env
ten0s/centos6_otp16.3-1_build-env   v1                  6a6cb6d22232        45 minutes ago      1.047 GB
$ popd
</pre>

* Check the environment image

<pre>
# Notice absent of command to run
$ docker run -ti ten0s/centos6_otp16.3-1_build-env:v1
Supported commands:

Usage: build PROJECT VERSION [OS=centos6]
Example: build kelly 1.2.3

</pre>

<pre>
$ docker run -ti ten0s/centos6_otp16.3-1_build-env:v1 build
Usage: build PROJECT VERSION [OS=centos6]
Example: build kelly 1.2.3
</pre>

* Project building helper utility

<pre>
$ bin/build
Usage: build PROJECT VERSION [OS=centos6]
Example: build kelly 1.2.3
</pre>

* Build [smppload](https://github.com/PowerMeMobile/smppload)

<pre>
$ bin/build smppload 1.3.0
...
Build SUCCEEDED: /home/ten0s/projects/docker/tmp.ubc7ILh8Aw/smppload-1.3.0-centos6.x86_64.tar.gz
</pre>