import os
import subprocess
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('autocreat_github.conf')

dirp = os.path.join(config.get('init', 'local_init_repo'), config.get('init', 'init_repo_name'))
init_repo_url = config.get('init', 'github_init_repo')

if not os.path.exists(dirp):
  os.makedirs(dirp) 
os.chdir(dirp)
print subprocess.Popen("git clone " + init_repo_url, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()
