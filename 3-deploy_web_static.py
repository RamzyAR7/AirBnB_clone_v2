#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers,
using the function deploy
"""

from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.237.93.225', '54.172.137.10']
env.key_filename = ['~/.ssh/id_rsa']


def do_pack():
    """Packs the web_static files into a .tgz file"""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        folder_name = archive_path.split("/")[-1][:-4]
        run("mkdir -p /data/web_static/releases/{}/".format(folder_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(folder_name, folder_name))
        run("rm /tmp/{}.tgz".format(folder_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(folder_name, folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(folder_name))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Deploys web_static to web servers"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
