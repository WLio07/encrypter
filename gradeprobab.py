import math
q, i, n = int(input("How many options in each question? ")), int(input("How many questions in the exam? ")), int(input("How many questions would you like to get right? "))
def probac(q, i, n):
	prob =  (((math.factorial(q))/(math.factorial(n)*math.factorial(q-n))) * ((1/i)**n) * (((i-1)/i)**(q-n)))*100 #calculates the likelihood and converts it into base 100
	return prob
print("The likelihood of randomly marking {} questions correctly in an exam of {} questions with {} options each is of {}%" .format(n, q, i, probac(q, i, n))) 	
input("Press ENTER to exit the program.")
