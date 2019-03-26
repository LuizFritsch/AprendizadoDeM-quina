#from FuncoesAuxiliares import *
#from FuncoesEstatisticas import *
from math import *
from numpy import *
import pandas as np
import arquivos as a

#
def hipotese(x, th0, th1):
	return th0 + th1 * x

#Le os dados e armazena na matriz
dataset=a.readtable("x03.txt")

#Taxa de aprendizado, quanto menor o alfa, 
alpha=0.0001

#Funcao pra achar a melhor reta
def treinar(x,y,alpha):
	qtdAmostras=len(x)
	#Nao entendi qual deve ser exatamente o theta 0 e theta 1 iniciais
	theta0=0.0
	theta1=1.0
	#taxa de erro
	erro=666
	#Condicao de parada: so para quando a taxa de erro for maior que 0.00001
	while(erro>0.00001):

		dtheta0=0.0
		dtheta1=0.0
		for i in range(0,qtdAmostras):
			dtheta0=dtheta0+(theta0+theta1*x[i])-y[i]
			dtheta1=dtheta1+((theta0+theta1*x[i])-y[i])*x[i]
		tempt0=theta0
		tempt1=theta1
		theta0=theta0-alpha*dtheta0/qtdAmostras
		theta1=theta1-alpha*dtheta1/qtdAmostras
		print('---------------')
		print('-',erro,'-')
		print('---------------')
		erro=math.sqrt((theta0-tempt0)**2+(theta1-tempt1)**2)
	plot(x,y,"bo")
	#ynovo=[hipotese(i,theta0,theta1) for i in x]
	#plot (x,ynovo,"r",linewidth=3,label='modelo')
	show()
	return[theta0, theta1]

x = asarray(a.column(dataset,2))
y = asarray(a.column(dataset,3))
print (treinar(x, y, alpha))



'''
Regressao Linear com múltiplas features
n = nmr de features (Ou caracteristicas)
m = nmr de amostras 
Antes havia X de i = Feature de entrada da i-ésima amostra (coluna x)
Agora ha Xj de i = Feature de J na i-ésima amostra de treinamento
Antes h(x) = teta0+teta1*x
Agora h(x) = teta0+teta1*X1(constante = 1)+teta2*X2+tetan*Xn
x=[x0,x1,xn] pertence aos Reais^n+1
teta=[teta0,teta1,tetan] pertence aos Reais^n+1
h0(x) = Somatorio de i=0 até n xi*tetai ou teta^T*x
Gradiente =
	h0(x) = teta^T*x = teta0*x0(=1) + teta1*x1 + ... tetan*xn
	j(teta) = 1/2m * somatorio de i = 1 até m (h0(x^i)-y^i)^2
	tetaj = tetaj-alpha*(derivada/(derivada*tetaj))*j(teta)
	tetaj = tetaj-alpha*(1/m) * somatorio de i = 1 * (h0(x^i)-y^i)*x^i na i
	teta0 = teta0-alpha(1/m) * somatorio de i = 1 ate m * h0(x^i)-j^i) x0^i
	teta1 = teta1-alpha(1/m) * somatorio de i = 1 ate m * h0(x^i)-j^i) x1^i

feature scaling=
	-1<=xi<=1
xi passe a ser x1-largura


alpha = alpha0*e^-lambda(t-tmax)

'''

