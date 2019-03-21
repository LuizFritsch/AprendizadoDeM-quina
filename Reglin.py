from arquivos import *
from math import *
from numpy import *
import pandas as np

def hipotese(x, th0, th1):
	return th0 + th1 * x

dataset=readtable("x06.txt")

alfa=0.0001

def treinar(x,y,alpha):
	qtdAmostras=len(x)
	theta0=0.0
	theta1=1.0
	erro=666
	while(erro>0.001):
		dtheta0=0.0
		dtheta1=0.0
		for i in range(0,qtdAmostras):
			dtheta0=dtheta0+(theta0+theta1*x[i])-y[i]
			dtheta1=dtheta1+((theta0+theta1*x[i])-y[i])*x[i]
		tempt0=theta0
		tempt1=theta1
		theta0=theta0-alpha*dtheta0/qtdAmostras
		theta1=theta1-alpha*dtheta1/qtdAmostras
		erro=math.sqrt((theta0-tempt0)**2+(theta1-tempt1)**2)
	plot (x, y, "bo")
	plot (x, [hipotese(i, theta0, theta1) for i in x], "r", linewidth=3, label='modelo')
	show()
	return[theta0, theta1]

x = asarray(column(dataset,2))
y = asarray(column(dataset,3))
print treinar(x, y, alfa)
