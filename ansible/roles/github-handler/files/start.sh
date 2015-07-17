#!/bin/bash

cd /opt/py3-venv/ && source bin/activate
cd gh-handler && python handler.py >>/tmp/gh-handler.out.log 2>>/tmp/gh-handler.err.log


