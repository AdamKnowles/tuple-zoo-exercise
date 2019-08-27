# Create a tuple named zoo that contains 10 of your favorite animals.
# Find one of your animals using the tuple.index(value) syntax on the tuple.
# # Example
# flowers = ("daisy", "rose")
# flower.index("rose") # Output is 1
# Determine if an animal is in your tuple by using value in tuple syntax.
# animal_to_find = "kangaroo"
# if animal_to_find in zoo:
#     # Print that the animal was found
# You can reverse engineer (unpack) a tuple into another tuple with the following syntax.
# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"
# Create a variable for the animals in your zoo tuple, and print them to the console.
# Convert your tuple into a list.
# Use extend() to add three more animals to your zoo.
# Convert the list back into a tuple.

zoo = list(("zebra", "lion", "mongoose", "hyena", "elephant", "meerkat", "warthog", "lemur", "antelope", "boar"))

(first_animal, second_animal, third_animal, fourth_animal, fifth_animal, sixth_animal, seventh_animal, eighth_animal, ninth_animal, tenth_animal) = zoo





print(zoo[0])
print(zoo.index("lion"))
zoo.extend(["cat", "dog"])

animal_to_find = "lion"
if animal_to_find in zoo:
    print("animal found!")


for animal in zoo:
    print(animal)

new_zoo = tuple(list(("zebra", "lion", "mongoose", "hyena", "elephant", "meerkat", "warthog", "lemur", "antelope", "boar")))

print(new_zoo)





    



    