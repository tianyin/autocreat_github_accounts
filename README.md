### Automatically create GitHub accounts, import source code, and add collaborators

#### 1. Check teams
If you are using a team file, you can use `check_teams.py` to check if one student is included in multiple teams (which is not allowed). `teamtemplate.csv` is a template for team file.
```
python check_teams.py $teamfile
```

#### 2. Create Github repos
Before creating repos, you need to config those fields in `autocreat_github.conf`
- netrc_file 
  - the uname/password file for github login, create the file following `netrcc-template`
- github_init_repo
  - the initial code repo from which the generated repos will import code
-org_name
  - coure organization
- repo_prefix
  - name prefix of the generated repos
  
`main.py` is the script for generating a repo, import source code, and add collaborators. You can run by
```
python main.py --team="geoff tianyin karthik"
```
or 
```
python main.py --team-file="$team_file"
```
Before you do that, you need to do some configurations at `autocreat_github.conf`, rename `netrcc-template` to `netrcc` and put your github account/pw there (don't upload the new `netrcc`). Also, this script is hard-coded for FA16 class, and if you want to reuse, you need to rename some of the URLs. 

For logging, you can dump into a local file.
```
python main.py --team="geoff tianyin karthik" | tee run.log


