palavra1 = input()
palavra2 = input()
palavra3 = input()
if palavra1 == 'vertebrado' and palavra2 == 'ave' and palavra3 == 'carnivoro':
    resultado = 'aguia'
if palavra1 == 'vertebrado' and palavra2 == 'ave' and palavra3 == 'onivoro':
    resultado = 'pomba'
if palavra1 == 'vertebrado' and palavra2 == 'mamifero' and palavra3 == 'onivoro':
    resultado = 'homem'
if palavra1 == 'vertebrado' and palavra2 == 'mamifero' and palavra3 == 'herbivoro':
    resultado = 'vaca'
if palavra1 == 'invertebrado' and palavra2 == 'inseto' and palavra3 == 'hematofago':
    resultado = 'pulga'
if palavra1 == 'invertebrado' and palavra2 == 'inseto' and palavra3 == 'herbivoro':
    resultado = 'lagarta'
if palavra1 == 'invertebrado' and palavra2 == 'anelideo' and palavra3 == 'hematofago':
    resultado = 'sanguessuga'
if palavra1 == 'invertebrado' and palavra2 == 'anelideo' and palavra3 == 'onivoro':
    resultado = 'minhoca'
print(resultado)

