import FuncoesAuxiliares as f
import pandas as pd

'''
#Dados do primeiro dataset sobre peso do corpo e peso do cerebro
'''
resultado = f.readtable("Dados.txt")

dados_df = pd.DataFrame(resultado, columns=['index','brainw','bodyw'])

dados_df = dados_df.drop('index',axis=1)

print (dados_df)
'''
#
'''
