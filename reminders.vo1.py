Mtime = int(input("Whst hour is it? (0-23)"))

if (Mtime <= 5):
    print("Its early . You should be sleeping")
elif (Mtime <=7):
    print("wake up,brew that coffee,get that mile run in,and get that brekfast...")
elif(Mtime <= 9):
	print("Time to go to work.")
elif(Mtime <= 12):
	print("You should be working!")
elif(Mtime <= 13):
	print("Take your lunch break!")
elif(Mtime <= 17):
	print("Do you feel that afternoon lull?")
elif(Mtime <= 19):
	print("Time to hit the gym…")
elif(Mtime <= 21):
	print("Gotta eat that dinner.")
elif(Mtime <= 23):
	print("Get that SLEEP. And rePEAT!")
else:
	print("You didn’t type an acceptable value! (0-23")
