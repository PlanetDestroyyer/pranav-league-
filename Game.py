import random
def game(comp,you):
	if comp=='w':
		if you =='w':
			print("Drawn")
		elif you =='s':
			print("You win")
		elif you =='g':
			print("You loss")
	elif comp =='s':
		if you =='w':
			print("U loss")
		elif you =='w':
			print("Draw")
		elif you =='g':
			print("U win")
	elif comp =='g':
		if you == 'w':
			print("U win")
		elif you =='s':
			print("U loss")
		elif you =='g':
			print("Draw")
	else :
		print("Error")
print("Comouter's Turn : Snake(s),Water(w)and Gun(g)")
randno = random.randint(1,3)
print(randno)
if randno==1:
	comp='s'
elif randno ==2:
	comp ='w'
elif randno ==3:
	comp ='g'
else:
	print("Error")
you = input("Make your choice : Snake(s),Water(w) and Gun(g)")
print(game(comp,you))