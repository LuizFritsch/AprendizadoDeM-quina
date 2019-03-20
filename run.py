import pandas as pd
import FuncoesAuxiliares as f
import pandas as pd
import RegressaoLinear as rl
import numpy as np
import matplotlib.pyplot as plt

'''
#Dados do primeiro dataset sobre peso do corpo e peso do cerebro
'''
resultado = f.readtable("DadosPesoCerebroXpesoCorpo.txt")

dados_df = pd.DataFrame(resultado, columns=['index','brainw','bodyw'])


dados_df = dados_df.drop('index',axis=1)

rl = rl.RegressaoLinear(2, 0, dados_df, 0.1, 60) 
#print (rl.retornaFuncaoCusto('brainw','bodyw'))
print (rl.calculaGradienteDescendente('brainw','bodyw'))

plt.scatter(dados_df['brainw'], dados_df['bodyw']) 