import pandas as pd
import matplotlib.pyplot as plt
from carro import Carro
import leitorInputs

#grafico 1

numBranco = leitorInputs.cores.count('Branco')
numPreto = leitorInputs.cores.count('Preto')
numPrata = leitorInputs.cores.count('Prata')
numAzul = leitorInputs.cores.count('Azul')
numCores=[numBranco, numPreto, numPrata, numAzul]
nomecores=['Branco', 'Preto', 'Prata', 'Azul']
plt.pie(numCores, labels=nomecores, colors=['White', 'Black', 'Silver', 'Blue'],
        wedgeprops={'edgecolor': 'black'})
plt.title('Cores dos Carros')
plt.show()


#grafico 2

numAuto = leitorInputs.cambios.count('Automático')
numManu = leitorInputs.cambios.count('Manual')
camb = ['Manual', 'Automático']
plt.bar(camb, [numManu, numAuto], color='Red')
plt.title('Opção de câmbio dos veículos')
plt.show()


#grafico 3

plt.scatter(leitorInputs.cores, leitorInputs.kms)
plt.title('Quilometragem dos carros de acordo com a cor')
plt.show()


#grafico 4

plt.scatter(leitorInputs.kms, leitorInputs.anos)
plt.title('Correspondência do ano do carro com sua quilometragem')
plt.show()