import csv
import sys

def check_teams(teamcsvfile):
  teammap = {}
  students = {}
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
        teammap[tid] = team
      for student in team:
        __add2map(students, student, tid)

  print '#students:', len(students)
  print '#teams:   ', len(teammap)
  #checking 
  for student in students:
    if len(students[student]) > 1:
      sys.exit(student + ' is in more than one team: ' + str(students[student]))
 
def __add2map(smap, student, team):
  if student not in smap:
    smap[student] = []
  smap[student].append(team)

def __add2team(team, student):
  student = student.strip()
  if len(student) > 0:
    team.append(student)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print 'check_teams team_file'
  else:
    print sys.argv 
    #check_teams(sys.argv[0])
    check_teams(sys.argv[1])
