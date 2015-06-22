## Prerequisites

In order to make the below steps to work you need to have [Python 3.x](http://linuxsysconfig.com/2013/03/running-multiple-python-versions-on-centos6rhel6sl6/) and [Pip](https://pip.pypa.io/en/latest/installing.html)
installed.


## Usate

* Install virtualenv:

<pre>
$ sudo pip install -U virtualenv
$ virtualenv -p python3 --no-site-packages /tmp/v-env/
$ source /opt/v-env/bin/activate
</pre>


* Install needed modules:

<pre>
$ pip install -r requirements.txt
</pre>

* Run Bottle server:

<pre>
$ python handler.py
</pre>

## NOTE
By default this github hook's handler running at *:4321.
You can change this behaviour simply by editing the last string of code in main file:

<pre>
$ tail -n 1 handler.py 
    run(host='0.0.0.0', port=4321)
</pre>