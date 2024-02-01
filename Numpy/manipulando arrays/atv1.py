import numpy as np
from array_especies import especies

#a - Selecione a segunda coluna com a quantidade de espécies encontradas e adicione em um array as qtd_especies
qtd_especies = especies[:,1]
#b - De qtd_especies selecione apenas as primeiras 3 quantidades e print
print(qtd_especies[:3])
#c - Print as 5 últimas quantidades de espécies
print(qtd_especies[-5:])
#d - Crie um array que contenha apenas os tamanhos das espécies e ordene por ordem crescente
tamanho_especies = np.sort(especies[:,3])
print(tamanho_especies)