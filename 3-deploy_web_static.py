#!/usr/bin/python3
"""Import required modules"""
from fabric.api import *
from datetime import datetime
import os

env.hosts = ["52.91.118.245", "100.26.50.62"]


def do_pack():
    """This method generates a tgz archive from the contents of
    the web_static folder"""
    current_datetime = datetime.now()

    archive_name = current_datetime.strftime("web_static_%Y%m%d%H%M%S.tgz")

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local(f"tar -czvf versions/{archive_name} web_static")

    if result.succeeded:
        return f"versions/{archive_name}"
    else:
        return False


def do_deploy(archive_path):
    """This method distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        original_filename = os.path.basename(archive_path)
        filename_without_ext = os.path.basename(archive_path).split(".")[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp")
        run("mkdir -p {}{}/".format(path, filename_without_ext))

        run(
            "tar -xzf /tmp/{} -C {}{}/".format(
                original_filename, path, filename_without_ext
            )
        )

        run("rm /tmp/{}".format(original_filename))

        run("mv {0}{1}/web_static/* {0}{1}/"
            .format(path, filename_without_ext))

        run("rm -rf {}{}/web_static".format(path, filename_without_ext))

        run("rm -rf /data/web_static/current")

        run("ln -s {}{}/ /data/web_static/current"
            .format(path, filename_without_ext))
        return True
    except Exception as e:
        return False


def deploy():
    """This method creates and distributes an archive to web servers"""
    archive_path = do_pack()
    return do_deploy(archive_path)
