#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from
the contents of the web_static """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ creating .tgz file """
    d = datetime.utcnow()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(d.year,
                                                             d.month,
                                                             d.day,
                                                             d.hour,
                                                             d.minute,
                                                             d.second)
    if local("mkdir -p versions").failed is True:
        return None
    if local("tar -czf {} web_static".format(filename)).failed is True:
        return None
    return filename
