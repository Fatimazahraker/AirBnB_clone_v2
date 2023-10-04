#!/usr/bin/python3
""" archive the static """

from fabric.api import task, local
from datetime import datetime


@task
def do_pack():
    """ method doc"""

    now = datetime.now()
    timeformat = now.strftime('%Y%m%d%H%M%S')
    archivename = f'web_static_{timeformat}.tgz'
    archivepath = 'versions'
    mkdir = f"mkdir -p {archivepath}"
    path = f"{archivepath}/{archivename}"
    print(f"Packing web_static to {path}")
    local(f"{mkdir}&& tar -cvzf {path} web_static")
