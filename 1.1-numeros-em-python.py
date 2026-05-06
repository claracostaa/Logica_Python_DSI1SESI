# AULA COMPLETA: NUMEROS EM PYTHON
"""
Vamos aprender:
1 - Tipos numéricos
2 - Conversões de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5 - Coerção de tipos
6 - Verificação de tipos
7 - Entrada de dados
"""
# PASSO 01 - TIPOS NUMÉRICOS
# int - Inteiros
# float - números com casas decimais
# complex - números complexos (usado em matemática/engenharia)

print ("===== TIPO NÚMERICOS =====")

# EXEMPLO 01 - NÚMERO INTEIRO

#criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("Valor:", numero_inteiro)

#Type() mostra qual é o tipo da variável
print ("Tipo:", type(numero_inteiro))

print (-----------------------------)

# EXEMPLO 02 - NÚMEROS DECIMAL

#Float é um número com ponto decimal
numero_decimal = 3.14

print ("Valor:", numero_decimal)
print ("Type:", type(numero_decimal))

print ("-----------------------------")
# EXEMPLO 03 - NÚMEROS COMPLEXOS

#Um número complexo possui duas partes:
#Parte real(número normal)
#Parte imaginária (multiplicada por j)

#Estrutura Geral:
#numero = a + bj

#a = parte real
#b = parte imaginária
#j = unidade imaginária

numero_complexo = 2 + 3j

print ("Valor:", numero_complexo)
print ("Type:", type(numero_complexo))

print ("-----------------------------")
