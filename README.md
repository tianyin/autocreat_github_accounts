### Automatically create GitHub accounts, import source code, and add collaborators

#### 1. Check teams
If you are using a team file, you can use `check_teams.py` to check if one student is included in multiple teams (which is not allowed).
```
python check_teams.py $teamfile
```

#### 2. Create Github repos
`main.py` is the script for generating a repo, import source code, and add collaborators. You can run by
```
python main.py --team="geoff tianyin karthik"
```
or 
```
python main.py --team-file="$team_file"
```
Before you do that, you need to do some configurations at `autocreat_github.conf`. Also, this script is hard-coded for FA16 class, and if you want to reuse, you need to rename some of the URLs. 

For logging, you can dump into a local file.
```
python main.py --team="geoff tianyin karthik" | tee run.log


