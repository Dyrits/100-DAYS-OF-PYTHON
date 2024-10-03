countries = ["India", "USA", "UK", "Canada", "Australia"]

# Accessing elements in a list
india = countries[0]
australia = countries[-1]
print(india, australia, sep="\n")

# Modifying elements in a list
countries[0] = "Bharat"
print(countries)

# Adding elements to a list
countries.append("New Zealand")
countries.extend(["Germany", "France"])
print(countries)

# Inserting elements into a list
countries.insert(1, "China")
print(countries)

# Removing elements from a list
countries.remove("UK")
print(countries)


