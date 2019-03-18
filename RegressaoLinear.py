import pandas as pd
import FuncoesAuxiliares as f

class RegressaoLinear:
    def __init__(self, teta0,teta1,dadosRegressao):
        self.t0 = teta0
        self.t1 = teta1
        self.dados = dadosRegressao

    def retornaPredicao(self, x):
        return self.t0+(self.t1*x)

    def retornaFuncaoCusto(self, column1, column2):
        soma = 0
        for i in self.dados.itertuples():
            soma += (self.retornaPredicao(float(i[column1]))-float(i[column2]))**2
        return soma/(2*(len(self.dados)))


