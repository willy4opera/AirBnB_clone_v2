#!/usr/bin/python3
# Fabfile: Automates the generation of .tgz
# archive from the contents of web_static.

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Here, we created the tar gzipped archive of web_static."""
    date_t = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_t.year,
                                                         date_t.month,
                                                         date_t.day,
                                                         date_t.hour,
                                                         date_t.minute,
                                                         date_t.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
