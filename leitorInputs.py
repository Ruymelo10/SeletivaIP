import os
from carro import Carro
entradas = os.listdir('./inputs')

cores=[]
anos=[]
kms=[]
cambios=[]
modelos=[]
for arquivo in entradas:
    with open('./inputs/'+arquivo, 'r', encoding='utf8') as f:
        cor = 'Não Informado'
        ano = 'Não Informado'
        km = 'Não Informado'
        cambio = 'Não Informado'

        linha = f.readlines()
        for i in range(0, len(linha)):
            if linha[i] == 'COR\n' or linha[i] == 'Cor\n':
                cor = linha[i+1].replace('\n','')
            if linha[i] == 'ANO\n' or linha[i] == 'Ano\n':
                ano = linha[i+1].replace('\n','')
            if linha[i] == 'KM\n' or linha[i] == 'Quilometragem\n':
                km = linha[i+1].replace('\n','')
            if linha[i] == 'Câmbio\n':
                cambio = linha[i+1].replace('\n','')

        carro = Carro(cor, ano, km, cambio)
        cores.append(cor)
        anos.append(ano)
        kms.append(km)
        cambios.append(cambio)
