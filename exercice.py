#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	# le nom est séparé lorsqu'il trouve '-' et chacun des nom est dans une liste
	name = name.split('-')[0]


	#Mettre majuscule la première lettre et minuscule les autres
	mise_en_forme = name[0].capitalize() + name[1:].lower()

	return f"Bonjour {mise_en_forme}"

def get_random_sentence(animals, adjectives, fruits):
	phrase = 'Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s'

	animal_word = animals[random.randrange(0, len(animals))]
	adject_word = adjectives[random.randrange(0, len(adjectives))]
	fruits_word = fruits[random.randrange(0, len(fruits))]

	return f"Aujourd’hui, j’ai vu un {animal_word} s’emparer d’un panier {adject_word} plein de {fruits_word}"

def encrypt(text, shift):

	code_cryptage = 
	print(text)
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
