#!/usr/bin/python3
"""Import required modules"""
from fabric.api import *
from fabric.context_managers import cd
import os

env.hosts = ["52.91.118.245", "100.26.50.62"]


def do_deploy(archive_path):
    """This method distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        archive_filename = os.path.basename(archive_path).split(".")[0]

        put(archive_path, "/tmp")
        run("mkdir -p /data/web_static/releases/{}".format(archive_filename))

        with cd("/data/web_static/releases/{}".format(archive_filename)):
            run("tar -xzf /tmp/{} --strip-components=1"
                .format(os.path.basename(archive_path)))

        run("rm -rf /tmp/{}".format(os.path.basename(archive_path)))

        run("rm -rf /data/web_static/current")

        run(
            f"ln -sF /data/web_static/releases/{archive_filename} \
            /data/web_static/current"
            )
        return True
    except Exception as e:
        return False
