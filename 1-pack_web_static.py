#!/usr/bin/python3
"""fab script that generates a tgz file"""
import os.path
import datetime
from fabric.api import run, local


def do_pack():
    """function that generates a tgz file"""
    time = strftime("%Y%M%d%H%M%S")
    local('mkdir -p versions')
    try:
        filename = f'versions/web_static_{time}.tgz'
        local(f'tar -cvzf  versions/web_static_{time}.tgz web_static/')
        return filename
    except Exception:
        return None
