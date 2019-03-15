from pylab import *
from random import *
from statistics import *
from math import *

# !/usr/bin/python

#aux functions
def menordovetor(vetor):
	menor = vetor[0];
	for i in range(0,size(vetor)):
		if( menor > vetor[i] ):
			menor = vetor[i]
	return menor


def maiordovetor( vetor ):
	maior = vetor[0];
	for i in range(0,size(vetor)):
		if( maior < vetor[i] ):
			maior = vetor[i]
	return maior


##Calculos estatisticos

#amplitude total
def amplitudetotal(vetor):
	return maiordovetor( vetor ) - menordovetor(vetor)


#media
def avg( a ):
	av=0.0 
	for i in range (0,size(a)):
		av=av+a[i]
	return av/size(a)

#varianca
def varianca(a):
	media = avg(a)
	soma = 0.0
	for i in range (0,size(a)):
		soma = soma + ( ( a[i] - media ) ** 2 )
	varin = soma/size(a)	
	return varin

#desviopadrao
def desviopadrao(a):
	return sqrt(varianca(a));

#coeficientedevariacao
def coeficientedevariacao(vetor):
	return (desviopadrao(vetor)/ avg(vetor))*100

#mediana
def mediana(amostra):
	amostra.sort()
	tamanho = len(amostra)
	meio = tamanho/2

	if( tamanho % 2 == 1 ):
		return amostra[meio]
	else:	
		y = int( floor( meio ) )
		x = int( ceil( meio ) )	
		return (amostra[y] + amostra[x-1]) / 2.0

#moda
def moda(a):                                                                                 
	repeticoes = 0
	vetor = []
	for i in a:
		vetor.append( floor(i) )		                                                                         
	for i in vetor:                                                                              
    		aparicoes = vetor.count(i)                                                             
    		if aparicoes > repeticoes:                                                       
        		repeticoes = aparicoes                                                       
                                                                                         
	modas = []                                                                               
	for i in vetor:                                                                           
    		aparicoes = vetor.count(i)                                                             
    		if aparicoes == repeticoes and i not in modas:                                   
        		modas.append(i)                                                                  
                                                                                         
	return modas 
#######################################
def indexOf(n,v):
	x = 0
	for i in v:
		if( i == n ):
			return x
		x = x+1
	return -1

def quartis(a):
	median=mediana(a)
	b1=[]
	b2=[]
	b3=[]
	#b4=[]
	if(size(a)%2 == 1):
		for i in range(0,size(a)/2):
			b1.append(a[i])
			b2.append(a[i+size(a)/2+1])
	else:
		for i in range(0,size(a)/2):
			b1.append(a[i])
			b2.append(a[i+size(a)/2])
	quartil1=mediana(b1)
	quartil3=mediana(b2)
	data = [floor(quartil1), floor(median), floor(quartil3)]
	return data  

#graficos
##barras
def grafico(a):
	y=range(0,size(a))
	plot (y,a,"ro")
	xlabel('SAMPLE')
	ylabel('DATA')
	show()

##histograma
def histograma(a, titulo, eixox, eixoy ):
	hist(a)
	title(titulo)
	xlabel(eixox)
	ylabel(eixoy)
	show()

##Boxplot
def boxplots( data ):
	# basic plot
	boxplot(data)
	show()

#########################
def toFloat(vetor):
	aux = []
	for linha in vetor:
		aux.append( float(linha) )
	return aux
#########################

##histograma
def histograma(a, titulo, eixox, eixoy ):
	hist(a)
	title(titulo)
	xlabel(eixox)
	ylabel(eixoy)
	show()

