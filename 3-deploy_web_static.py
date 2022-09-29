#!/usr/bin/python3
# prepare tar file
from fabric.api import local, run, put
from time import strftime
import os
from fabric.state import env

env.hosts = ['18.232.187.106', '18.206.13.226']


def do_pack():
    """generate .tgz archive"""
    timenow = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        filepath = "versions/web_static_{}.tgz".format(timenow)
        local("tar -cvzf {} web_static/".format(filepath))
        return filepath
    except Exception:
        return None


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


def deploy():
    """creates and distributes archive to webserver"""
    try:
        new_archive = do_pack()
        return do_deploy(new_archive)
    except Exception:
        return False
