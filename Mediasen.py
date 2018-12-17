m = int(input("Enter 1 for arithmetic mean, 2 for weighted average, 3 for geometric mean, 4 for harmonic mean: "))
valo, pes, i = [], [], 1
n = int(input("Number of values whose mean will be calculated? "))
while i <= n:
	val = float(input("Insert the {}º value: " .format(i)))
	valo.append(val)
	if m == 2:
		pe = float(input("Insert the weight of this value: "))
		pes.append(pe)
		valo[i-1] = valo[i-1]*pe
	i += 1
x = 1
if m == 1:
	x = sum(valo)/i
elif m == 2:
	x = sum(valo)/sum(pes)
elif m == 3:
	for t in valo:
		x *= t
	x = x**(1/n)
elif m == 4:
	x = 1/(sum(1/u for u in valo)/n)
print()
print("The {} is {}." .format("arithmetic mean" if m == 1 else "weighted average" if m == 2 else "geometric mean" if m == 3 else "harmonic mean", x), end='\n\n')
input("Press ENTER to exit the program.")