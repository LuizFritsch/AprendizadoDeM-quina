import pandas as pd
import FuncoesAuxiliares as f
import numpy as np
class RegressaoLinear:
    def __init__(self, teta0,teta1,dadosRegressao):
        self.t0 = teta0
        self.t1 = teta1
        self.dados = dadosRegressao

    def retornaPredicao(self, x):
        return self.t0+(self.t1*x)

    def retornaFuncaoCusto(self, column1, column2):
        soma = 0
        print 
        for index, row in self.dados.iterrows():
            soma += ((self.retornaPredicao(np.float(row[column1]))-np.float(row[column2]))**2)
        print (soma)
        return soma/(2*(len(self.dados)))


