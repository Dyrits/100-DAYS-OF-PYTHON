states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Get the length of the list
print(f"There are {len(states_of_america)} states in the United States of America.")

# Merge two lists
states_of_america.extend(["Puerto Rico", "Guam"])
print(states_of_america)
states_of_america += ["U.S. Virgin Islands", "American Samoa"]
print(states_of_america)
states_of_america = [*states_of_america, "Northern Mariana Islands"]
print(states_of_america)