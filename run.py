import pandas as pd
import FuncoesAuxiliares as f
import pandas as pd
import RegressaoLinear as rl
'''
#Dados do primeiro dataset sobre peso do corpo e peso do cerebro
'''
resultado = f.readtable("DadosPesoCerebroXpesoCorpo.txt")

dados_df = pd.DataFrame(resultado, columns=['index','brainw','bodyw'])


dados_df = dados_df.drop('index',axis=1)

rl = rl.RegressaoLinear(2, 0, dados_df)
print (rl.retornaFuncaoCusto('brainw','bodyw'))

