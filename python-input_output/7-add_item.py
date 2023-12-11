#!/usr/bin/python3

import sys
import json
from os import path

# Define the function to save an object to a JSON file
def save_to_json_file(my_obj, filename):
    # Open the file in write mode using the with statement
    with open(filename, 'w') as f:
        # Write the object to the file in JSON format using the json.dump() method
        json.dump(my_obj, f)

# Define the function to load an object from a JSON file
def load_from_json_file(filename):
    # Open the file in read mode using the with statement
    with open(filename, 'r') as f:
        # Load the object from the file in JSON format using the json.load() method
        obj = json.load(f)
    # Return the object
    return obj

# Set the filename for the JSON file
filename = 'add_item.json'

# If the file does not exist, create an empty list and save it to the file
if not path.exists(filename):
    save_to_json_file([], filename)

# Load the contents of the JSON file into a list
my_list = load_from_json_file(filename)

# Add the command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)

# Print the updated list
print(my_list)
