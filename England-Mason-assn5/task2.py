# Mason England
# CS 1400 - MWF 8:30


import random


# make a class for animals
class Animal:
    def __init__(self, type: str, amount: int, sound: str):
        self.type = type
        self.amount = amount
        self.sound = sound


animals = []

# welcome message
print("Welcome to the animal mix o matic, the machine that makes the wackiest animals you can dream of")
print("\n")

print("for three different animals you have seen recently enter the fallowing,")

#inputs for the animals
for i in range(3):
    animal_type = input("    Type of the animal: ")
    amount = int(input("    number of them seen: "))
    sound = input("    What sound does this animal make?: ")

    animals.append(Animal(animal_type, amount, sound))
    print("\n")

input("press enter to see the results: ")
print("\n")

# calculate all of the results
print(F"    the total number of animals seen is {animals[0].amount + animals[1].amount + animals[2].amount}")
print(F"    the types of animals seen were {animals[0].type}s, {animals[1].type}s, and {animals[2].type}s")
print(F"        {animals[0].type}s say {animals[0].sound}.\n        {animals[1].type}s say {animals[1].sound}.\n        {animals[2].type}s say {animals[2].sound}")

#string scrambling smaple code
average_amount = (animals[0].amount + animals[1].amount + animals[2].amount) / 3
animal_name = animals[0].type + animals[1].type + animals[2].type
word_list = list(animal_name)
random.shuffle(word_list)
animal_name = "".join(word_list)

animal_sound = animals[0].sound + animals[1].sound + animals[2].sound
word_list2 = list(animal_sound)
random.shuffle(word_list2)
animal_sound = "".join(word_list2)

print("\n")
print(F"the animal mix o matic mixed together these animals and made {int(average_amount)} {animal_name}'s that all say {animal_sound}")