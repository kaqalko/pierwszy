test = 5 
print("pre ->"+str(test))
def lolz():
	test = 8 
	print("func ->"+str(test))
	def funkcja2():
		print("transmitancja")
lolz()
print("post ->"str(test))