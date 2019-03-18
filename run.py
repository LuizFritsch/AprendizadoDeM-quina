import FuncoesAuxiliares as f
import pandas as pd

'''
#Dados do primeiro dataset sobre peso do corpo e peso do cerebro
'''
resultado = f.readtable("Dados.txt")

dados_df = pd.DataFrame(resultado, columns=['index','brainw','bodyw'])

dados_df = dados_df.drop('index',axis=1)

print (dados_df.head(6))

'''
#Funcao para achar o erro (distancia do y até o ponto) em cada ponto,
#ou popularmente chamada de erro quadrado médio
'''
def erroEmCadaPonto_OU_erroQuadradoMedio(amostra):
	tamanhoAmostra = len(amostra)
	(1/2*tamanhoAmostra)*()

'''
#Funcao gradiente descendente(QUE DESCE, DIG DÃ) pra achar a partir de qual ponto a reta começa a subir
'''
def gradienteDescendente():
	deltaJ = deltaJ - (alfa*derivada/derivadaDeDeltaJ)*J()
