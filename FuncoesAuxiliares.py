# !/usr/bin/python

def writefilestring(name,string):
	f = open(name, 'w')
	f.write(string+"\n")
	f.close()

def writefile(name,array):
	f = open(name, 'w')
	for item in array:
		f.write(str(item)+"\n")
	f.close()

def column(matrix, i):
    return [float(row[i]) for row in matrix]

def readtable(name):
	f = open(name, 'r')
	lines = f.readlines()
	result = []
	for x in lines:
		result.append(x)
	f.close()
	tabela = []
	for x in range(0,len(result)):
		mydata=filter(None, (result[x].strip()).split(" ") )
		if (mydata):
			tabela.append(mydata)
	return tabela

def readfile(name, column):
	f = open(name, 'r')
	lines=f.readlines()
	result=[]
	for x in lines:
		if (x.strip()):
			elem=(x.split(' ')[column]).strip()
			number=float(elem)
			result.append(number)
	f.close()
	return result

def readFile(name, columns):
	f=open(name,"r")
	lines=f.readlines()
	result=[]
	for x in lines:
		for y in range(0,columns):
			result.append(x.split(' ')[y])
	f.close()
	df = pd.DataFrame(result, columns=['index'])
	
	return result