meals = ["eggs", "more eggs", "spaghetti bolognas"]

meals_as_a_dictionary = {
    "breakfast" : "eggs",
    "lunch" : "more eggs",
    "dinner" : "spaghetti bolognas"
}

print(meals_as_a_dictionary["breakfast"])
print(meals_as_a_dictionary["lunch"])
print("breakfast" in meals_as_a_dictionary)
print(meals_as_a_dictionary.keys())
# print(getatribute(meals_as_a_dictionary["eggs"]))

meals_as_a_dictionary["lunch"] = "bacon"
print(meals_as_a_dictionary["lunch"])
del(meals_as_a_dictionary["breakfast"])
# print(meals_as_a_dictionary[:"more guys"])
print(list(meals_as_a_dictionary))


