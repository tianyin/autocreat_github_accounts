import os
import subprocess
import time

def check_status(ret, statuscode):
  return 'Status: ' + str(statuscode) in ret

def creat_repo(repo_name, netrcf):
  """
  Create a repository on GitHub using the given name
  API ref.: https://developer.github.com/v3/repos/ 
  """
  param = '\'{"name": "%s", '\
      '"description":"Nachos for CSE 120", '\
      '"private": true, '\
      '"has_issues": true, '\
      '"has_wiki": true}\'' % repo_name
  #print param
  #creat_cmd = 'curl -i -u ' + ':'.join(crd) +  ' https://api.github.com/orgs/ucsd-cse120-fa16/repos -d ' + param
  creat_cmd = 'curl -i --netrc-file ' + netrcf +  ' https://api.github.com/orgs/ucsd-cse120-fa16/repos -d ' + param
  proc = subprocess.Popen(creat_cmd, 
      shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (out, err) = proc.communicate()
  ret = check_status(out, 201)
  if ret == False:
    print out
    print err
  return ret 

def import_code(repo_name, netrcf):
  """
  Import the source code into the repo
  API ref.: https://developer.github.com/v3/migration/source_imports/
  Note that this API is in the 'preview' mode so GitHub requires to add the accept header 
  """
  crd = __getcrd(netrcf)
  param = '\'{"vcs": "git", '\
      '"vcs_url": "https://github.com/ucsd-cse120-fa16/cse120-proj.git", '\
      '"vcs_username": "%s", "vcs_password":"%s"}\'' % (crd[0], crd[1])
  #import_cmd = ('curl -i -u ' + ':'.join(crd) + ' -X PUT https://api.github.com/repos/ucsd-cse120-fa16/%s/import -d ' % repo_name) + param + ' -H \'Accept: application/vnd.github.barred-rock-preview\''
  import_cmd = ('curl -i --netrc-file ' + netrcf + ' -X PUT https://api.github.com/repos/ucsd-cse120-fa16/%s/import -d ' % repo_name) + param + ' -H \'Accept: application/vnd.github.barred-rock-preview\''
  proc = subprocess.Popen(import_cmd, 
        shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (out, err) = proc.communicate()
  ret = check_status(out, 201)
  if ret == False:
    print out
    print err
  return ret 

def add_collaborators(repo_name, student, netrcf):
  """
  Add the student as a collaborator for the given repo
  API ref.: https://developer.github.com/v3/repos/collaborators/ 
  """
  addco_cmd = 'curl -i --netrc-file ' + netrcf + ' -X PUT -d \'\' https://api.github.com/repos/ucsd-cse120-fa16/%s/collaborators/%s' % (repo_name, student)
  #print addco_cmd
  proc = subprocess.Popen(addco_cmd, 
        shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  (out, err) = proc.communicate()
  ret = check_status(out, 204)
  if ret == False:
    print out
    print err
  return ret 

def __gen_repo_name(team):
  """
  team should in the form of a list [student1, student2, student3]
  """
  return 'nachos_fa16_' + '_'.join(sorted(team))

def __getcrd(netrcf):
  with open(netrcf, 'rb') as f:
     l = f.read().strip()
     uname = l[l.rfind('login') + len('login'):].strip()
     uname = uname[:uname.find(' ')]
     passw = l[l.rfind('password') + len('password'):].strip()
     return [uname, passw]

def creat_all(team, netrcf, wait=1):
  """
  Creat the repo, add the collaborators, and init the source code
  """
  print '-----------------------------------------'
  print team
  repo_name = __gen_repo_name(team)
  #print repo_name
  
  if creat_repo(repo_name, netrcf) == False:
    print 'create repo [' + repo_name + '] failed!'
    return
  else:
    print 'create repo [' + repo_name + '] succeeded!'
  
  if import_code(repo_name, netrcf) == False:
    print 'import repo [' + repo_name + '] failed!'
    return
  else:
    print 'import repo [' + repo_name + '] succeeded!'

  for student in team:
    if add_collaborators(repo_name, student, netrcf) == False:
      print 'addco [' + student + '] to [' + repo_name + '] failed!'
      return
    else:
      print 'addco [' + student + '] to [' + repo_name + '] succeeded!'

  time.sleep(wait) 
