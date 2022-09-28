#!/usr/bin/env python3
"""fabscript that generates a tgz file"""
import os.path
import datetime
from time import strftime

from fabric.api import run, local

time = strftime("%Y%M%d%H%M%S")


def do_pack():
    """function that generates a tgz file"""
    local('mkdir -p versions')
    try:
        local(f'tar -cvzf  versions/web_static_{time}.tgz web_static/')
        return
    except Exception:
        return None
