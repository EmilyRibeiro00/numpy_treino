import numpy as np
from array_especies import especies

#letra a - Usando um index boolean crie um array que contém os dados da maior espécie encontrada (considerando o seu tamanho), esse valor 
#corresponde ao valor 22.
indice_maior_especie = np.where(especies[:,3]==22) #retorna um array booleano
print("Dados da maior espécie: ",especies[indice_maior_especie]) 

#letra b - Usando fency index faça um array que contém apenas dados da espécie com ID 297.
filtro = especies[:,0] == 297 #retorna array booleano
print("Dados da espécie de ID 297: ",especies[filtro])  

#letra c - Usando np.where() faça um array com a linha com dados correspondentes a espécie com 105 representantes encontrados.
especie_selecionada_105_rep = np.where(especies[:,1]==105)
print("Dados da espécie que contém 105 representantes: ",especies[especie_selecionada_105_rep]) 

#letra d - Considere a profundeza em que o espécie foi encontrada substitua valores maiores que 60 com "Profundo”
especies_modificada = np.where(especies[:, 2] > 60, "Profundo", especies[:, 2]) #Substituindo valores maiores que 60 na coluna de profundidade 
array_modificado = especies
array_modificado = especies.astype(str) #mudando o tipo do array
array_modificado[:, 2] = especies_modificada #Substituindo a coluna modificada na copia do array
print("Array modificado, incluindo a coluna modificada:\n",array_modificado) 
