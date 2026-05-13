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

print("===== TIPO NÚMERICOS =====")

# EXEMPLO 01 - NÚMERO INTEIRO

#criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print("Valor:", numero_inteiro)

#Type() mostra qual é o tipo da variável
print ("Type:", type(numero_inteiro))

print ("-----------------------------")

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

#EXEMPLO 03 - ACESSO CADA PARTE DO NÚMERO

#.REAL RETORNA A PARTE REAL
print ("Parte Real:", numero_complexo.real)
#.imag retorna a parte imaginária
print ("Parte Imaginaria:", numero_complexo.imag)

#PASSO 02 - CONVERSÃO TIPOS
# Apenas para separar visualmente a saída no terminal
print("\n\n")
##Exemplo Classico:
## Dadods vindos do usuário são sempre do tipo string, muitas vezes é necessário converter eles

print ("===== conversões =====")

# float - int

valor = int (3.9)

print ("int (3.9):", valor)
print ("Tipo:", type(valor))

#STRING -> int
valor1 = "10"
print(type(valor1))
print("int (valor1):", int(valor1))
print("Tipo:", type(int(valor1)))

valor2 = int ("10")
print('int("10"):', valor2)
print("tipo", type(valor2))

#int --> Float
valor3 = float (10)
print ("float(10):", valor3)
print ("Tipo:", type(valor3))
