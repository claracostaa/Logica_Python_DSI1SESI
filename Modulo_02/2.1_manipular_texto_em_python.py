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
