# PYTHON  LIST - Lista com python

'''
Uma lista, em python, determina que podemos ter um conjunto de dados composto por qualquer tipo de valor - ou seja, data types diferentes podem compor uma mesma lista!
'''

# definir uma lista - para este proposito criaremos uma variavel e, à ela, atribuiremos uma valor que será descrito da seguinte forma: o uso do caractere []COLCHETE, atribuido a qualquer variavel CRIA UMA LISTA - EM PYTHON!

#           0      1       2               3             4               

umaLista = [1, 'palavra', 'c', 'ASDHFASDHFASDIHFAISU', 256.8]

#               0          1                          2          
#                                       0        1            2             3
#                                                        0       1      2

listona = [    74,     'Sopranos',   ['Python', 879, ['xalala', 532.7, 12], 50]          ]

print('===================== LISTAS ================')
print()
print('------------------- exibindo as listas --------------------')
print(umaLista)
print(listona)

print('------------------- algumas operações com listas --------------------')
print('listona no index 2: ', listona[2])
print('acessar 879 de listona: ', listona[2][1])
print('acessar 532.7 de listona: ', listona[2][2][1])
print('acessar 12 de listona: ', listona[2][2][2])

# ---------------------------------------------------------------------------

print()
print('===================== outras manipulações ================')

#              0         1     2          3            4           5
lingProg = ['Python', 'Java', 'C#', 'Visual Basic', 'Cobol', 'Javascript', 'C', 'Objective-C e Swift', 'Zurk', 'a']
#               5        4     3          2            1           0       -1
print(lingProg[2]) # saida: C#
print(lingProg[1:]) # saida: 'Java', 'C#', 'Visual Basic', 'Cobol', 'Javascript'
print('qual a saida: ', lingProg[-1])
print('qual a saida: ', lingProg[-2])
print('e esta saida? : ', lingProg[1::-1])
print('e agora? : ', lingProg[::-1]) # aqui, a saida está invertida 

'''
print('e esta saida? : ', lingProg[1::-1]) -> lê-se da seguinte forma: 

1º valor: start -> onde o "fatiamento" começa!
* valor entre os dois :--: stop -> está vazio - aqui é onde o "fatiamento" termina! nesta caso, não temos indice posicional

2º valor: step -> o "passo", ou seja, o intervalo entre os elementos -> significa que vamos "de traz para frente" percorrendo toda a lista

*** ou seja, estamos invertendo os "fatiamentos"
'''

# ---------------------------------------------------------------------------
print()
print('===================== USO DE FUNÇÕES NATIVAS ================')
print()

# uso da função len()
print(len(lingProg)) # para obter o numero total de dados dentro do conjunto

# uso da função max()
print(max(lingProg)) # para observar a lista e encontrar o valor maximo dentro dela

# uso da função min()
print(min(lingProg)) # para observar a lista e encontrar o valor minimo dentro dela

# <     >


diferentona = ['%ython', ')ava', 'C#', '#isual Basic', '1', '4']

print(min(diferentona))
print(max(diferentona))