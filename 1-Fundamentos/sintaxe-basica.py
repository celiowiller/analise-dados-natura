# AULA 1
print('Hello Mundo Python!')

# esta é uma linha de comentário no python; este é, então, o famoso comentário de linha
# portanto, estes textos não aparecerão na tela fwpjfvE~]P/HNGIB    outgb´[24]

'''
este é um comentario de bloco 
posso colocar, aqui, varias linhas que ainda assim não 
aparecerão no resultado da execução do meu codigo
'''

# ======================================================================================

# AULA 2

print("======================== ESTUDO DE VARIAVEIS ======================")
print()

# passo 1: vamos definir duas variaveis - e vamos chama-las de a e b
# variavel, para qualquer linguagem de programação, nada mais é do que uma "alocação/reserva" de "espaço" - na memória do seu computador - para guardar algum valor que, posteriormente, iremos manipular

a = 3 # declaramos uma variavel com o nome (a)e atribuimos à ela o valor 1; para que pudesse ocorrer este atribuição de valor fizemos uso do operador =(igual) (operador de atribuição)

b = 2 # declaramos uma variavel com o nome (b)e atribuimos à ela o valor 2; para que pudesse ocorrer este atribuição de valor fizemos uso do operador =(igual) (operador de atribuição)
print('Valor da variavel a: ', a) # nesta instrução estamos fazendo o seguinte: "imprimindo/exibindo" na tela, um texto e o valor de uma variavel - que aparecerá ao lado do texto
print('Valor da variavel b: ', b)

# agora, vamos criar uma nova variavel; vamos chama-la de variavel (c); esta variavel receberá como valor uma operação de soma; esta operação vai realizar a soma das variaveis a e b
c = a + b # aqui, usamos o caractere + -> significa que, neste momento, ele assume o "papel" de ser um operador, python, de soma matematica 
print('O valor da variavel c é: ', c)

print()
print('---- outros operadores python (subtração, multiplicação, divisão) -----')

# abaixo serão implementadas algumas novas operações com o uso dos operadores aritmeticos
print('Resultado da subtração de a - b = ', a - b)
print('Resultado da multiplicação de a x b = ', a * b)
print('Resultado da divisão de a / b = ', a / b)

print()
print('---------------- operadores especiais ------------------')

# observar os operadores especiais - aritmeticos - python
print('Resultado do módulo  de a "%" b = ', a % b) # esta é uma operação de divisão onde, o elemento mais importante é: o RESTO DA DIVISÃO -> MÓDULO

print('Resultado da exponenciação entre a e b -> a ** b = ', a ** b) # aqui, estamos elevando a variavel (a) ao valor da variavel (b)

# ==============================================================================
print()
print('====================== INFERENCIA DE TIPO ========================== ')

# declarar 3 novas variaveis
numUm = 560
NumDois = 458.79
NOME = 'Chilindrina'

# fazer uso da função print() para exibir os valores das variaveis
print('--------------------- valores das variaveis ------------------------')
print(numUm)
print(NumDois)
print(NOME)
print()

print('--------------------- tipos das variaveis ------------------------')
# observar os data types de cada variavel
print(type(numUm)) # função type tem origem no python core - sua tarefa é exibir o data type - ou seja - o tipo de dado de uma variavel
print(type(NumDois))
print(type(NOME))
print()


print('====================== ATRIBUIÇÃO MULTIPLA DE VALORES ========================== ')

# criar UMA variavel e, com ela, praticar a atribuição multipla de valores 
print('--------------------- atribuição sequencial de variaveis ------------------------')
y = l = z = m = Natura = 1000

print(Natura)
print(y)
print(l)
print(z)
print(m)

print()
print('--------------------- atribuição multipla ------------------------')

h, d, j, t = 63, 56.89, 'c', 'Felipes'

print(h, d, j, t)
print(d, h, t, j)

print()
print('====================== MANIPULAÇÃO DE STRINGS ========================== ')
# Vamos definir umanova variavel
umaFrase = 'Hoje é um dia excelente!'

# neste passo, serão exibidos os valores das manipulções aplicadas a string umaFrase
print('--------------------- manipulando a string ------------------------')

print(umaFrase) # aqui estamos exibindo o valor da variavel umaFrase
print(type(umaFrase)) # aqui, estamos observando seu data type

print(umaFrase[0]) # aqui, o caractere [](colchete) assume a funcionalidade de "cortar/fatiar" a string num determinado "pedaço"; neste caso estamos selecionando/fatiando/cortando o valor da variavel - umaFrase - a partir da indicação do indice posicional que um determinado ocupa - aqui, o indice posicional 0 (zero) ocupado pela letra H

'''
abaixo, na sequencia numérica que vamos indicar está descrito os denominados INDICES POSICIONAIS DE UM CONJUNTO DE VALORES/DADOS - indice que é associado/ocupado por um determinado valor 
         0   1  2   3 4  5 6  7 8  9  10  11   12  13  14  15  16 17 18 19 20  21  22
         H   o  j   e    é    u m      d  i    a    e   x  c   e   l  e  n  t  e   !

'''


print(umaFrase[2:12]) # aqui, estamso fazendo a seleção não só de um valor mas de intervalo de valores - que começa no indice posicional 2 e vai até o indice posicional 10. Este intervalo de valores - subcojunto - é determinado pelo uso do caractere (:) dois pontos - que, em termos simples, quer dizer: "me da este valor que comeca aqui e vai até ali - 2 até 10"



print(umaFrase[:8])
print(umaFrase[3:])
print(umaFrase + ' Muito bom! Que o dia todo seja assim!')
