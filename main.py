import get_teams
import creat_repos
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('autocreat_github.conf')

teams = get_teams.get_teams(config.get('global', 'team_file'))
print '#teams: ', len(teams)
print teams

for team in teams:
  creat_repos.creat_all(team, config.get('global', 'netrc_file'))
