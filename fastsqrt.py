import math


x = int(input("X: "))
n = int(input("Iterations: "))
initguess = x >> (int(math.log10(x)+1))
print('\n')
print("Initial guess is: " + str(initguess))


for i in range(n):
	initguess = 0.5 * (initguess + x/initguess)
	print("Guess " + str(i) + ": " + str(initguess))


print("Final Approximation: " + str(initguess))
print("Actual sqrt by sqrt() function: " + str(math.sqrt(x)))
print("% accuracy: " + str(round(abs(1-initguess/x)*100,2)) + "%")
