#!/usr/bin/python3
"""
Fabric script that generates a
tgz archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        time_now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(time_now)
        local("tar -cvzf {} web_static".format(archive_path))

        if os.path.exists(archive_path):
            return archive_path
        else:
            return None
    except Exception:
        return None