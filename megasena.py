#!/usr/bin/python
# megasena estimativa
# -- coding: utf-8 --
# Criado por Carlos Eugenio
# Boa Sorte a todos

import random
#Listas

grupo1 = [1,2,11,12]
grupo2 = [3,4,13,14]
grupo3 = [5,6,15,16]
grupo4 = [7,8,17,18]
grupo5 = [9,10,19,20]
grupo6 = [21,22,31,32]
grupo7 = [23,24,33,34]
grupo8 = [25,26,35,36]
grupo9 = [27,28,37,38]
grupo10 = [29,30,39,40]
grupo11 = [41,42,51,52]
grupo12 = [43,44,53,54]
grupo13 = [45,46,55,56]
grupo14 = [47,48,57,58]
grupo15 = [49,50,59,60]

resultado = random.choice(grupo1),random.choice(grupo2),random.choice(grupo3),random.choice(grupo4),random.choice(grupo5),random.choice(grupo6),random.choice(grupo7),random.choice(grupo8),random.choice(grupo9),random.choice(grupo10),random.choice(grupo11),random.choice(grupo12),random.choice(grupo13),random.choice(grupo14),random.choice(grupo15)

jogo = [resultado[i] for i in sorted(random.sample(xrange(len(resultado)),6))]

print "Bom Jogo Boa Sorte !!! >>> %s" % jogo
