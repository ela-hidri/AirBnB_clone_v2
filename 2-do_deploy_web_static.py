#!/usr/bin/python3
""" that distributes an archive to your web servers,
using the function do_deploy"""
from datetime import datetime
from fabric.api import env, put, run
import os.path

env.hosts = ["100.26.244.46", "52.91.126.18"]


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
