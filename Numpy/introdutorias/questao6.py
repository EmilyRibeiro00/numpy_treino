import random
import numpy as np

#6 - Crie um array que irá representar a cartilha desses jogos de bingo. Os números das suas cartelas variam entre 1 e 30, e você terá 
#10 participantes. Cada cartela terá 12 números (4, 3). Crie um array que representa esse jogo.
print("\nQuestão 6")
cartela = np.random.randint(1,30,size=(10,4,3))
print(cartela)
