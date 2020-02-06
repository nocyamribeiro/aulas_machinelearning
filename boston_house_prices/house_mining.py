#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:03:23 2020

@author: maycon
"""

from scipy.stats import pearsonr

import pandas as pd

dataframe = pd.read_csv('/home/maycon/Documentos/MBA/Machine Learning/house.csv')

columnNames = dataframe.columns

correlacoes = dataframe.corr(method ='pearson')

correlacoes

descricao = dataframe.describe();

print("Nomes das colunas")
print(columnNames)

var = 'lstat'

dataframe.plot.scatter(x=var, y='medv')


print ('pearson coef =', pearsonr(dataframe[var], dataframe['medv']))

for col in columnNames:
        dataframe.plot.scatter(x=col, y='medv')
        
        
for col in columnNames:
        print()
        
        