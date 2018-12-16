print("Given three dots on a Cartesian plane:")
lpontos, leixo, lcoord = ['A', 'B', 'C'], ['abscissa', 'ordinates'],[] #list of dots, list of axis, list of dots' coordinates
for i in lpontos:
	for u in leixo:
		pos = float(input("Enter the position of the dots {} on the axis {}: " .format(i, u))) #[Aabs, Aord, Babs, Bord, Cabs, Cord]
		lcoord.append(pos)
ldistancias, lpdph0, lpdph2 = [], [2, 5, 4, 2, 5, 4], [1, 0, 3]
for i,u in zip(lpdph0, range(0, 3)):
	x = float(((abs(lcoord[i] - lcoord[u])**2) + (abs((lcoord[u + 3]) - (lcoord[lpdph2[u]]))**2))**(1/2))
	ldistancias.append(x)
#the three dots connect, forming a triangle
perimetro_triang = sum(ldistancias)
sp = perimetro_triang/2   #sp == semiperimeter
area_triang = abs((sp*(sp - ldistancias[0])*(sp - ldistancias[1])*(sp - ldistancias[2])))**(1/2)
print("u.l. = unity of lenght", "u.a.² = unity of area", "The distance between A and B in u.l. is {}".format(ldistancias[0]), "The distance between A and C in u.l. is {}".format(ldistancias[1]), "The distance between B and C in u.l. is {}".format(ldistancias[2]), sep='\n')
if (perimetro_triang!=0):
	if(area_triang>0):
		print("Upon connecting these three dots, a triangle will be formed.", "This triangle will have:", "Semiperimeter of {} u.l..".format(sp), "Perimeter of {} u.l..".format(perimetro_triang), "Area of {} u.a.².".format(area_triang), "Side AB of {} u.l..".format(ldistancias[0]), "Side AC of {} u.l..".format(ldistancias[1]), "Side BC of {} u.l..".format(ldistancias[2]), sep='\n')
	elif (area_triang==0):
		print("Upon connecting these three dots, a line of", sp, "u.l. lenght will be formed.")	
input("Press ENTER to exit the program.")
