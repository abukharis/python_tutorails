file = open("team1.txt", "a+")

team=['manun\n','mancity\n','liverpool\n','sheffiledun\n','chelsea' ]

for i in range(5):
    new_team=team[i]
    file.write(new_team)

file.close()
file =open('team1.txt','r')
for i in range(5):
    if i==0:
       #file.read()
       print(file.readline())
    elif i==3:
        #file.read()
        print(file.readline())
    else:
        file.readline()
file =open('team1.txt','r+')
for i in range (5):
    if i==0:
        file.write('this is a new line')
    else:
        new_team=team[i]
        file.write(new_team)
file.close 