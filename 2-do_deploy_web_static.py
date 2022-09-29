#!/usr/bin/python3
# prepare tar file
from fabric.api import local, put, run
from time import strftime
from fabric.state import env


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


env.hosts = ['18.232.187.106', '18.206.13.226']


def do_deploy(archive_path):
    """distributes archive to web server"""
    filename = archive_path.split('.')[0]
    filename = filename.split('/')[1]
    filename_full = filename + '.tgz'
    try:
        put(archive_path, "/tmp/")
        print(filename)
        print(archive_path)
        run(f'tar xzvf /tmp/{filename_full} -C /data/web_static/releases/')
        run(f'mv /data/web_static/releases/web_static '
            f'/data/web_static/releases/{filename}')
        run(f'sudo rm -rf /tmp/{filename_full}')
        run('sudo rm /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{filename} '
            f'/data/web_static/current')
        return True
    except Exception:
        return False
