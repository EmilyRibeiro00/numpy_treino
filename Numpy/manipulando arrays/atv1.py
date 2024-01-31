import numpy as np

#1 - Explorando Ecossistemas
#ID da espécie, quantidade de representantes encontrados, profundeza, tamanho médio da espécie.

especies = np.array([[747, 89, 33, 5],
[623, 123, 32, 13],
[501, 22, 49, 2],
[116, 101, 42, 10],
[297, 56, 69, 22],
[613, 64, 27, 7],
[295, 84, 29, 14],
[692, 105, 72, 16],
[229, 103, 35, 5],
[374, 124, 70, 1]])

#a - Selecione a segunda coluna com a quantidade de espécies encontradas e adicione em um array as qtd_especies
qtd_especies = especies[:,1]
#b - De qtd_especies selecione apenas as primeiras 3 quantidades e print
print(qtd_especies[:3])
#c - Print as 5 últimas quantidades de espécies
print(qtd_especies[-5:])
#d - Crie um array que contenha apenas os tamanhos das espécies e ordene por ordem crescente
tamanho_especies = np.sort(especies[:,3])
print(tamanho_especies)