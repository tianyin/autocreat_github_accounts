import get_teams
import creat_repos
import ConfigParser
import argparse
import sys

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Create github repos for the given teams')
  parser.add_argument('--team-file', dest='team_file', help='team_3.csv'),
  parser.add_argument('--team', dest='team', help='github_id_1 github_id_2 github_id3')
  args = parser.parse_args()

  config = ConfigParser.ConfigParser()
  config.read('autocreat_github.conf')

  if args.team:
    team = args.team.split()
    if len(team) > 3:
       print 'The team can have at most 3 members, but you have', len(team), 'members.'
    creat_repos.creat_all(team, config.get('global', 'netrc_file'))
    
  if args.team_file:
    teamf = config.get('global', 'team_file')
    print 'team_file:', teamf
    teams = get_teams.get_teams(teamf)
    print '#teams: ', len(teams)
    #print teams
    for team in teams:
      creat_repos.creat_all(team, config.get('global', 'netrc_file'))
