import os
import sys
import json
import time
import yaml
import subprocess
from threading import Thread
from bottle import run, request, route
from mail import send_mail


@route('/', method='POST')
def catcher ():
    data = dict(zip(['req_headers', 'req_body'], [dict(request.headers), request.json]))
    if data['req_headers']['X-Github-Event'] == 'create':
        t = Thread(target=create_handler, name='builder', args=(data,))
        t.start()
    else:
        print("Grac! We've got unhandled hook - '%s'!" % data['req_headers']['X-Github-Event'])
    return


def load_conf(proj):
    with open('config.yml', 'r') as f:
        c_cfg = yaml.safe_load(f)
        p_cfg = c_cfg['projects'][proj]
    return (c_cfg, p_cfg)


def create_handler(d):
    proj_name = d['req_body']['repository']['name']
    proj_vers = d['req_body']['ref']

    common_cfg, proj_cfg = load_conf(proj_name)

    build_script  = common_cfg['script']
    build_image   = common_cfg['image']

    send_from = common_cfg['send_from']
    send_to   = proj_cfg['notify']

    msg = 'See details in the attachment below\n' + common_cfg['storage_url']

    for dist in proj_cfg['dist']:

        ts = time.strftime("%Y%m%d%H%M%S", time.localtime())
        cmd = [build_script, proj_name, proj_vers, build_image.format(dist=dist), dist]
        flog = common_cfg['logfile'].format(timestamp=ts, project=proj_name, dist=dist)

        with open(flog, 'w') as build_out:
            p = subprocess.Popen(cmd, stdout=build_out, stderr=build_out)
            p.wait()
            if p.returncode:
                subj = "BUILD :: {proj} v{vers} ({dist}) :: FAILED !".format(proj=proj_name, vers=proj_vers, dist=dist)
            else:
                subj = "BUILD :: {proj} v{vers} ({dist}) :: SUCCEEDED !".format(proj=proj_name, vers=proj_vers, dist=dist)
        send_mail(send_from, send_to, subj, msg, files=[flog])


if __name__ == '__main__':
    run(host='0.0.0.0', port=4321)
