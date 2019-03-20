import pandas as pd
import FuncoesAuxiliares as f
import numpy as np

class RegressaoLinear:
    def __init__(self, teta0, teta1, dadosRegressao, alpha, qtVezes):
        self.t0 = teta0
        self.t1 = teta1
        self.dados = dadosRegressao
        self.alpha = alpha
        self.qtVezes = qtVezes

    def retornaPredicao(self, x):
        return self.t0+(self.t1*x)

    def retornaFuncaoCusto(self, column1, column2):
        soma = 0
        print 
        for index, row in self.dados.iterrows():
            soma += ((self.retornaPredicao(np.float(row[column1]))-np.float(row[column2]))**2)
        return soma/(2*(len(self.dados)))

    def calculaGradienteDescendente(self, column1, column2):
        tempT0 = self.t0
        tempT1 = self.t1
        i = 0
        while (i < self.qtVezes):
            for index, row in self.dados.iterrows():
                tempT0 += (-(1.0/len(self.dados))*(np.float(row[column2])-self.retornaPredicao(np.float(row[column1]))))
                tempT1 += (-(1.0/len(self.dados))*(np.float(row[column2])-self.retornaPredicao(np.float(row[column1])))*np.float(row[column1]))
            self.t0 -= tempT0*self.alpha
            self.t1 -= tempT1*self.alpha
            i += 1
        return [self.t0, self.t1]