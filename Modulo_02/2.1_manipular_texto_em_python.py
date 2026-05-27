# AULA COMPLETA - STRINGS EM PYTHON

# - Criação de strings
# - Strings multilinha
# - Indices e slices
# - Operações com strings
# - Imutabilidade
# - Método úteis
# - Formatação de texto
# - Unicode e bytee

# 1 - CRIAÇÃO DE STRINGS
# Strings são textos em python
# Podem ser criadas usando aspas simples ou duplas

texto1 = "Python"
texto2 = 'curso de Python'
texto3 = "Copa 'padrão fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1, texto2, texto3, texto4)

#Python permite misturar aspas simples e duplas, dentro das strings sem precisar escapar caracteres

# 2 - STRINGS MULTILINHA
# Usando três aspas (""" ou ''') para criar textos que ocupam várias linhas.
menu = """\
Uso: programa [OPÇÕES]
-h Exibe ajuda
-U Url do dataset
"""
print(menu)

#Esse formatp é muito usado para:
# - Menus
# - Documentação
# - Textos longos

# 3 - CONCATENAÇÃO AUTOMÁTICA
# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto = ("Copa" "2026" "Neymar é ultrapassado né?") 
print(texto)

# 4 - SRINGS COMO SEQUÊNCIAS
# Uma string funciona como uma sequência de caracteres, cada caractere possui um indice

st = "maracana"
print("Primeira Letra:", st[0])
# Só exibir a letra: m
 
print("ultima Letra:", st[-1])

print("Trecho 1:4:", st[1:4])

print("Do ínicio até 3:", st[:3])

print ("Do 2 até o fim:", st[2:])

print ("Tamanho:", len(st))

# 5 - OPERAÇÕES COM STRINGS
# Python permite várias operações com strings

print("m" in st)
# Significa que a letra "m" existe dentro da string

print("x" not in st)
# Significa que "X" não existe na string

print("m" * 3)
# Multiplicação repete a string

print("m" + "aracana" + texto1)
# Operador + concatena strings

# 6 - STRINGS SÃO IMUTÁVEIS
# Strings não podem ser alteradas diretamente!!!
# Isso siginifica que o conteúdo original não muda.
# O que acontece é a criação de uma nova strings

texto = "python 3"

# Método replace cria uma nova string
texto = texto.replace("3", "2")
print(texto)

# 7 - MÉTODOS IMPORTANTES
# Strings possuem vários métodos úteis.

cidade = "maracana"
# Coloca a primeira letra em maiúscula.
print(cidade.capitalize())

# Contar quantas vezes "a" aparece
print(cidade.count("a"))

# Verifica se começa com "m"
print(cidade.startswith("m"))

# Verifica se termina com "z"
print(cidade.endswith("z"))

frase = "copa de 2002"

print(frase.split(" "))

# 8 - FORMATAÇÃO DE STRINGS
