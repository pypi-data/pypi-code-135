from random import random
from math import ceil

all_dice = []

def maker(n):
	global all_dice
	def func():
		return ceil(random() * n)
	all_dice.append("d"+str(n))
	return func

d4 = maker(4)
d6 = maker(6)
d8 = maker(8)
d10 = maker(10)
d12 = maker(12)
d20 = maker(20)
d100 = maker(100)

def d()
	global all_dice
	return all_dice


