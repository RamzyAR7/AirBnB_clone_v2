#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric.api import run, put, env
import os


env.hosts = ['54.237.93.225', '54.172.137.10']
env.user = 'ubuntu'  # Assuming the username is 'ubuntu', change if needed
env.key_filename = ['~/.ssh/id_rsa']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        filename = os.path.basename(archive_path)
        folder_name = filename.split('.')[0]
        remote_path = "/tmp/{}".format(filename)
        release_path = "/data/web_static/releases/{}/".format(folder_name)

        put(archive_path, remote_path)
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(remote_path, release_path))
        run("rm {}".format(remote_path))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
