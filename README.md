### Automatically create GitHub accounts, import source code, and add collaborators

Before running the scripts, using `check_teams.py` to check the team file. We should not have one student joining two different teams.
```
python check_teams.py team3.csv
```

The configuration file is `autocreat_github.conf`. Change the `team_file` parameter everytime you run the scripts. 

`main.py` is the entry Python file to run the scripts. For logging, you can dump into a local file.
```
python main.py | tee run.log.3
```

