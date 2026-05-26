# agora, vamos começar a lidar  com elementos de maior complexidade
# portanto, vamos iniciar os codigos importando os recursos de módulo para que tudo funcione adequadamente
import numpy as np # aqui, a lib numpy recebe um "apelido", portanto, quando precisarmso referenciar a lib numpy basta escrever np

# criar duas matrizes - ambas receberão valores distintos
matriz1 = np.array([ [2, 4], [5, -6]  ]) # esta é a função array, com origem no numpy, especificamente usada para criar arrays

matriz2 = np.array([ [9, -4], [3, 5] ])


# definir a operação de soma das matrizes
matrizResultante = matriz1 + matriz2 

# exibir o resultado da soma das matrizes
print('O resultado da operação é: ', matrizResultante)
