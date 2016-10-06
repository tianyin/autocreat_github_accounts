import csv
import sys

def get_teams(teamcsvfile):
  teams = []
  teammap = {}
  with open(teamcsvfile, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvreader.next()
    for row in csvreader:
      team = []
      time = row[0]
      #tid = row[1]
      tid = row[2]
      __add2team(team, row[3])
      __add2team(team, row[4])
      __add2team(team, row[5])
      #reserved1 = row[6]
      #reserved2 = row[7]
      if len(team) == 0:
        sys.exit('[ERROR]' + tid + 'has no member!')
      else:
        teams.append(team)
      for student in team:
        __add2map(teammap, student, tid)

  #checking 
  for student in teammap:
    if len(teammap[student]) > 1:
      sys.exit(student + ' is in more than one team: ' + str(teammap[student]))
  
  return teams 

def __add2map(tmap, student, team):
  if student not in tmap:
    tmap[student] = []
  tmap[student].append(team)

def __add2team(team, student):
  student = student.strip()
  if len(student) > 0:
    team.append(student)
