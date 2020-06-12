import random
import msvcrt

w = 0
l = 0
d = 0
R = 0
while 1:
	R += 1
	print("Round %d"%R)
	k = input("Rock: 1, Paper: 2, Scissors: 3. Make Your Choice:")
	if k.isdigit() and float(k) >= 1 and float(k) <= 3:
		a = int(k)
		c = random.randint(1,3)
	else:
		print("Please type a integer number between 1 to 3!\n")
		continue


	if a == 1:
		yo = "Rock"
	elif a == 2:
		yo = "Paper"
	elif a == 3:
		yo = "Scissors"


	if c == 1: 
		co = "Rock"
	if c == 2:
		co = "Paper"
	if c == 3:
		co = "Scissors"

	print("You picked %s and Computer picked %s"%(yo,co))

	print("*"*50)

	if a == 3 and c == 2 or a != 3 and a > c and a <= 3 or a == 1 and c == 3:
		print("\nYou Win!\n")
		w += 1
	elif a == 1 and c == 2 or a != 1 and a < c and a >= 0 or a == 3 and c == 1:
		print("\nYou Lose!\n")
		l += 1
	elif a == c:
		print("\nDraw!\n")
		d += 1

	print("*"*50)


	print("Win  %d times"%w)
	print("Lose %d times"%l)
	print("Draw %d times\n"%d)


	# print("Continue or Press d to Exit")
	# if ord(msvcrt.getch()) == 68:
	# 	break
