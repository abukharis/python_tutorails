file = open("team2.txt", "w")

team=['manun\n','mancity\n','liverpool\n','sheffiledun\n','chelsea' ]
newfile ='\n'.join(team)
file.write(newfile)
file.close