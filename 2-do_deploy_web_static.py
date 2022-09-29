#!/usr/bin/python3
"""
deploy files to server
"""
from fabric.api import put, run
from fabric.state import env
import os
env.hosts = ['18.232.187.106', '18.206.13.226']


def do_deploy(archive_path):
    """distributes archive to web server"""
    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split('.')[0]
    filename = filename.split('/')[1]
    filename_full = filename + '.tgz'
    try:
        put(archive_path, "/tmp/")
        run('tar xzvf /tmp/{} -C '
            '/data/web_static/releases/'.format(filename_full))
        run('mv /data/web_static/releases/web_static '
            '/data/web_static/releases/{}'.format(filename))
        run('rm -rf /tmp/{}'.format(filename_full))
        run('rm /data/web_static/current')
        run('ln -s /data/web_static/releases/{} '
            '/data/web_static/current'.format(filename))
        return True
    except Exception:
        return False
