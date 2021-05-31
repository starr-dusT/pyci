# Imports
import tempfile
from config import config
import subprocess
import os

def clone_dir():
    tmp_dir = tempfile.mkdtemp()
    # TODO: update for Windows on work computers (this may not work)
    src_dir = tmp_dir + '/src'
    os.mkdir(src_dir)
    subprocess.call(['git', 'clone',
                     config['git_repo_location'],
                     tmp_dir + '/src'], stderr=subprocess.DEVNULL)
    return

def eval_state():
    clone_dir()
    return "running"
