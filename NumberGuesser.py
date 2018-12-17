import random
def randomg(min, max):
	r, g = random.randrange(min, max+1), None
	while g != r:
		print()
		g = int(input("Your guess: "))
		print()
		if g>max or g<min:
			print("That is not even in the range.") 
		elif g>r:
			print("Too high, try a lower number.")
		elif g<r: 
			print("Too low, try a higher number.")
	print("You got it.")	
print("This is number guesser, choose a range to generate a random integer from.")
print()
min, max = int(input("The minimum: ")), int(input("The maximum: "))
print("Range from {} to {} | ({}, {})" .format(min, max, min, max))
randomg(min, max)
input("Press ENTER to exit the program.")