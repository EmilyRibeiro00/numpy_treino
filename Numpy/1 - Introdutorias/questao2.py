import random
import numpy as np

#2 - Crie um array com valores inteiros, 3 linhas e 5 colunas com valores aleatórios.
print("\nQuestão 2")
array2 = np.random.randint(30,size=(3,4)) ## Gerar um array de 3 linhas e 4 colunas com números inteiros aleatórios entre 0 e 29
print(array2)
