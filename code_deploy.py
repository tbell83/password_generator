import subprocess


def deploy():
    subprocess.call(["git", "pull"])
