first_favorite_food = "sushi"
second_favorite_food = "burritos"
third_favorite_food = "burgers"
fourth_favorite_food = "ribs"
fifth_favorite_food = "spaghetti and meatalls"

# Let's put foods into a list.
# CRUD (Create, Read, Update, Delete)
# Create: name_of_list = ["first item","second item"]
fav_foods = ["sushi", "burritos","burgers","ribs","spaghetti and meatballs"]
print(fav_foods)

# Read the list by putting a number that matches the item we want (starting from 0, not 1)
print(fav_foods[0])
# What do I have to type to print "spaghetti and meatballs?"
print(fav_foods[4])

# Update
fav_foods[2] = "hot dogs"
print(fav_foods)

# Delete
fav_foods.remove("ribs")
print(fav_foods)


# print("I really like " + fav_foods[0])
# print("I really like " + fav_foods[1])
# print("I really like " + fav_foods[2])
# print("I really like " + fav_foods[3])

for i in range(8):
    print (i)

for i in range(4):
    print ("I really like " + fav_foods[i])

for thing in fav_foods:
    print ("I really love " + thing)

sentence = "I really like "
for food in fav_foods:
    sentence += food
    sentence += " and "
print(sentence)