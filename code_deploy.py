from subprocess import Popen, PIPE
import os


def deploy():
    cwd = os.path.dirname(os.path.realpath(__file__))
    p = Popen(['git', 'pull'], stdout=PIPE, stderr=PIPE, cwd=cwd)
    stdout, stderr = p.communicate()
    return stdout
