'''
um dicionario também é um conjunto de dados - da mesma forma que uma lista e uma string; mas  com algumas diferencas:

1 - para definirmos um dicionario é necessario usar os caracteres { } (chaves)

2 - um dicionario é composto por pares chave:valor -> key:value

3 - o conceito de indice posicional NÃO EXISTE par aum dicionario;
'''

# defini um dicionario

d = {
    # chave : valor
    # key   : value
    'Nome'  : 'Florinda',
    'idade' : 37,
    'Curso' : 'Clipper',
    20      : ' reais'
}

# exibir o dicionario
print('Este é o conteudo do dicionario: ', d)

print()
print('=================== OPERAÇÕES COM DICIONARIOS ==================')
print()

print('Imprimir o valor da key/chave [Nome]: ', d['Nome'])
print('Imprimir o valor da key/chave [idade]: ', d['idade'])
print('Imprimir os valores de todas as chaves/keys do dicionario:  ', d['Nome'], d['idade'], d['Curso'], d[20])

# até aqui, fizemos uso do processo de seleção de elementos key/chave do dicionario para exibir seus valores; também podemos fazer uso da função get()
print('-------------- uso da função get() --------------')

print(d.get('idade')) # aqui, com o uso da função get() temos um processo de seleção "indireta"

# ------------------------------------------------------------------------------

print()
print('-------------- processos de seleção --------------')
# observar a possibilidade de alterar valores definidos num dicionario
d['idade'] = 22
d['Nome'] = 'Clotilde'

# criar um novo par key/value
d['Sobrenome'] = 'Lalala'
print('Dicionario com novos valores: ', d)

# --------------------------------------------------------------
print()
print('-------------- novas formas de criar um dicionario --------------')

# nosso novo dicionario se chamará disciplinas
disciplinas = {}.fromkeys(['Historia', 'Matematica', 'Geografia'], 0)
print(disciplinas)

# neste passo, vamos criar uma estrutura de repetição - loop - para iterar sobre todos so valores do dicionario e exibir seus itens
for r in disciplinas.items():
    print(r)

'''
           1ª iteração          2ª iteração      3ª iteração    encerramento da repetição
 r .........................  ...............  ..............   ................ 
disciplinas = {'Historia': 0, 'Matematica': 0, 'Geografia': 0}

print(r) exibe o valor encontrado pela variavel na 1ª iteração 
('Historia', 0)

print(r) exibe o valor encontrado pela variavel na 2ª iteração 
('Matematica', 0)

print(r) exibe o valor encontrado pela variavel na 3ª iteração 
('Geografia', 0)


1º: o código, acima, é uma estrutura de repetição do python - for... in - que exibe todos os valores que forem encontrados o dicionario disciplinas!

2º: a variavel - r - é conhecida com variavel iteradora/auxiliar que irá RASTREAR/ITERAR sobre todos os valores que compõem o conjunto de dados 

3º: a função items() auxiliar na recuperação/rastreamento de todos os valores que compõem o dicionario - é ela que "aponta" quais serão os itens que devem ser rastreados - tudo isso ocorre " por debaixo dos panos" a partir do python core
items()
'''

print()
print('--------------------------------')

for x in d.items():
    print(x)