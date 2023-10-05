#!/usr/bin/python3
""" that distributes an archive to your web servers,
using the function do_deploy"""
from datetime import datetime
from fabric.api import env, put, run
import os.path

env.hosts = ["52.91.126.18", "100.26.244.46"]


def do_deploy(archive_path):
    """distribute an archive"""
    if os.path.isfile(archive_path) is False:
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    finally:
        return False
