"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

maior = 10 > 9 #true
maior_igual = 25 >= 25 #true
menor = 12 < 30 #true
menor_igual = 34 <= 50 #true
igual = 5 == 5 #true
diferente = 4 != 3 #true
igual2 = 'Joao' == 'Lucas' #false
diferente2 = 5 != 5 #false

lista = [maior, maior_igual, menor, menor_igual, igual, diferente, igual2, diferente2]
print(lista)