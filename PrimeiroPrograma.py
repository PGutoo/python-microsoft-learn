from datetime import date
import sys

# program.py
sum = 1 + 2
print(sum)

print("show this in the console")
# print["show this in the console"] Não funciona com colchetes

sum = 1 + 2 # 3
product = sum * 2
print(product)

# Tipos de dados

planets_in_solar_system = 8 #int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 #float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(distance_to_alpha_centauri)) ##<class 'float'> função type, identifica o tipo de dado

# Operadores

left_side = 10
right_side = 5
left_side / right_side # 2
# Sintaxe - Valor esquerdo <operador> Valor direito

# Operadores aritméticos + - / *

# Operadores de atribuição += -= /= *=

# Datas

today = date.today()
print(today)
#print("Today's date is: " + date.today()) # Da erro, porque o date.today() não é uma string
print("Today's date is: " + str(today))

# Argumentos de linha de comando

print(sys.argv)
print(sys.argv[0]) # program name
# print(sys.argv[1]) # first arg

# Entrada do usuário

print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number) # Cadeia de caracteres
print(int(first_number) + int(second_number)) # Converte para inteiro

