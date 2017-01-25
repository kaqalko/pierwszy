suma=0
elementy = []
def fibona(x):
	if x<2:
		return x
	else:
		return fibona(x-2) + fibona(x-1)
for x in range (1,4000000):
	elementy.append(fibona(x))
	pass
for element in elementy:
	if x%2==0 :
			suma=suma+x
print("Suma parzystych liczb w ciagu Fibonacciego do 4mil to: "+str(suma))

