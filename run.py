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
colors = np.random.rand(62)
area = (30 * np.random.rand(62))**2  # 0 to 15 point radii

plt.scatter(dados_df['brainw'], dados_df['bodyw'], s=area, c=colors, alpha=0.5)
plt.show() 