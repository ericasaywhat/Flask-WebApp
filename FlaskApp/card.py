"""
Python program that takes in a spreadsheet of medical terminology and makes flash cards

author: Erica J. Lee
updated: June 13,2016

"""
import random

dict= {
	'a(n)':'absence of a major part of the brain, skull, scalp',
	'ab':'removal of diseased organ away from the body',
	'acr(o)':'increased production of growth hormone in the body',
	'ad':'towards the center of the body'}


def flashcard(dict):
	key_list = dict.keys()
	rand_keys = random.choice(key_list)
	print rand_keys, ':', dict[rand_keys]


flashcard(dict)

