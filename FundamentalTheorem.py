def find_factors(n):
	L = []
	for x in range(1, n):
		if n % x == 0:
			L.append(x)
	if L == []:
		return False
	else:
		return L


def CharlesFundamentalTheorem(x):
#	x = int(input("Enter a number to factorise: "))

	Factors = find_factors(x)
	print("The factors of {} are {}\n".format(x, find_factors(x)))
	if Factors == False:
		return None
	temp = 1
	count = 0
	how_many = {}
	for factor in Factors:
		if factor > 1:
			while temp < x:
				count += 1
				temp += factor
				how_many[factor] = count
			count = 0
			temp = 1
	if Factors == [1]:
		return False
	else:
		return how_many
		
def apply():
	for x in range(30000000, 30000100):
		factors = CharlesFundamentalTheorem(x)
		if factors == False or factors == None:
			print("{} is prime ... \n".format(x))
		else:
			for k in factors:
				print("{} is {} x {}\n".format(x, k, factors[k]))
apply()

# Charles Truscott Watters. HarvardX MITx edX.org