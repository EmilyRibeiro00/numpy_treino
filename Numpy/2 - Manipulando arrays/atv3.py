import numpy as np
from array_especies import especies

#letra a - Adicione mais 2 espécies ao array: [[204, 10, 40, 12], [392, 11, 81, 11]].
novas_especies = np.array([[204, 10, 40, 12], [392, 11, 81, 11]])
adicionando_especies= np.concatenate((especies,novas_especies),axis=0)
print("Adicionando novas espécies:\n",adicionando_especies)
print("\n")

#letra b - Adicione mais uma coluna na no array original agora com o número de espécies encontradas com que indica se o animal enxerga ou não: 
#[0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0].
# Nova coluna a ser adicionada
nova_coluna = np.array([0, 1, 0, 0, 0, 0, 1, 0, 1, 1]).reshape((10,1))
adicionando_coluna = np.concatenate((especies,nova_coluna),axis=1)
print("Adicionando nova coluna:\n",adicionando_coluna)
