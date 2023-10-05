#!/usr/bin/python3
""" creates and distributes an archive to your web servers"""
from datetime import datetime
from fabric.api import local
from os.path import exists
from datetime import datetime
from fabric.api import env, put, run
import os.path

env.hosts = ["100.26.244.46", "52.91.126.18"]


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

def do_deploy(archive_path):
    """distribute an archive"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    tmp = "/tmp/{}".format(file)
    ohne_tgz = "/data/web_static/releases/".format(file.split(".")[0])
    try:
        put(archive_path, "/tmp/{}".format(file))
        run("mkdir -p {}/".format(ohne_tgz))
        run("tar -xzf {} -C {}".format(tmp, ohne_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(ohne_tgz, ohne_tgz))
        run("rm -rf {}/web_static".format(ohne_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except:
        return False

def deploy():
    """  creates and distributes an archive """
    new_path = do_pack()
    if exists(new_path) is False:
        return False
    result = do_deploy(new_path)
    return result
