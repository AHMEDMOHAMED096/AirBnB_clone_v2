"""Import required modules"""

from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """This method generates a tgz archive from the contents of the web_static"""
    current_datetime = datetime.now()

    archive_name = current_datetime.strftime("web_static_%Y%m%d%H%M%S.tgz")

    if not os.path.exists("versions"):
        os.makedirs("versions")

    result = local(f"tar -czvf versions/{archive_name} web_static")

    if result.succeeded:
        return f"versions/{archive_name}"
    else:
        return None
