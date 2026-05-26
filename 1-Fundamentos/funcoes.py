'''
UDF -> User Defined Function(Funções definidas pelo usuario)
funções que os programadores implementam.

Qual é a definição de função: em Python, uma função é definida a partir do uso da palavra reservada/comando  def!
função nada mais é do que um bloco codigo que pode cumprir uma ou mais tarefa para um determinado proposito!

descrição de uma função:

def -> nome_da_funcao ->():
    alguma(s) instrução(ões) que compõe(m) a função
    ou seja, as "tarefas" que a função irá cumprir.

    return -> expressão de retorno/resposta da função
'''

# abaixo, a definição da função exibir() terá um parametro: um parametro nada mais é do que uma variavel *** esta variavel/parametro será "enxergada/existirá" somente para a função 

def exibir(umTexto): # umTexto -> é o parametro - variavel local/pertencente unica e exclusivamente a esta função - em algum momento este parametro receberá algum valor 

    print(umTexto) # esta é a tarefa que a função cumprirá!  em que momento? Quando for chamada a sua execução!

# acima, a função exibir() foi definida; agora, precisamos chamar esta função à sua execução
# fazemos isso criando um CALLER - objeto chamador da função; 
exibir('Essa é 1ª chamada da função!')  # print() # items()
exibir('Esta é a 2ª chamada da função !')
exibir(9878962514321)
exibir(456.78)

print()
print('------------- função com uso de keyword/palavra-chave -------------------')

# definir uma nova função
def dados(nome, idade):
    # 1ª tarefa: exibir o valor associado ao parametro nome
    print('O nome é: ', nome)
    # 2ª tarefa: exibir o valor associado ao parametro idade
    print('A idade é: ', idade)
    # 3ª tarefa: é fazer uma verificação do valor da idade e exibir uma mensagem
    if idade >= 18: # esta expressão é conhecida com EXPRESSÃO DE TESTE
        # SE A AVALIAÇÃO FOR CONSIDERADA VERDADEIRA - TRUE, a tarefa abaixo será executada
        print('Pode entrar.')

    else: # mas, SE A AVALIAÇÃO FOR CONSIDERADA FALSA, a tarefa executada será esta abaixo 
        print('Sai fora de-menor!')
    # esta estrutura é conhecida como ESTRUTURA DE DECISÃO

    return # EXPRESSÃO QUE ENCERRA A FUNÇÃO

print('Função dados() será chamada')

dados(idade = 38, nome = 'Saul Goodman') # uso esporadico

#dados(38, 'Saul Goodman') # uso comum/frequente

print()
print('------------- função lambda -------------------')

'''
LAMBDA: em python, a função lambda é uma função ANÔNIMA - NÃO TEM NOME DEFINIDO; 
como uma função lambda não tem nome, precisamos associa-la ao um elemento que possa ser identificado/referenciado pelo seu nome -> isso que significa que: uma função lambda deve compor uma EXPRESSÃO DE FUNÇÃO; nada mais é do que uma variavel que recebe como valor uma função; assim, a função lambda pode ser chamada à sua execução  
'''

# vamos definir nossa função lambda
soma =  lambda valor1, valor2 : valor1 + valor2

'''
soma: variavel que recebe como valor  a função anonima/lambda

lambda: palavra reservada/comando que define a função

valor1, valor2: são os parametros da função lambda

valor1 + valor2: operação/tarefa que a função lambda cumpre
'''

# agora, precisamos chamar a função lambda à sua execução
print('O valor da soma - na função lambda - é: ', soma(100, 150))

# agora, precisamos chamar a função lambda à sua execução
print('Agora, o valor da soma - na função lambda - é: ', soma(5, -5))

