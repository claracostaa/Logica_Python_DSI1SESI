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
