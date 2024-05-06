#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives using the function do_clean
"""

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['54.237.93.225', '54.172.137.10']
env.key_filename = ['~/.ssh/id_rsa']


def do_clean(number=0):
    """Deletes out-of-date archives"""
    try:
        number = int(number)
        if number < 1:
            number = 1

        with lcd("versions"):
            local("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))

        with cd("/data/web_static/releases"):
            run("ls -t | tail -n +{} | xargs rm -rf".format(number + 1))
    except Exception as e:
        print(e)
        return False
