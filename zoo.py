import xml.etree.ElementTree as ET
import os
from enum import Enum

class MenuOptions(Enum):
    PRINT = "1"
    ADD = "2"
    DELETE = "3"
    SEARCH = "4"
    EXIT = "5"

# Dictionary to store animals
animal_data = {}

# Add function
def add():
    animal_name = input("Enter the name of the animal: ")
    animal_data[animal_name] = {}
    print(f"{animal_name} added to the list of animals.")

# Print function
def printdata():
    for animal in animal_data:
        print(f"Animal: {animal}")
        print()  # Add an empty line between animals

# Save function
def save_to_xml():
    root = ET.Element('animals')
    for animal in animal_data:
        animal_elem = ET.SubElement(root, 'animal', name=animal)
    
    tree = ET.ElementTree(root)
    tree.write('animal_data.xml')

# Load function
def load_from_xml():
    if os.path.exists('animal_data.xml'):
        tree = ET.parse('animal_data.xml')
        root = tree.getroot()
        for animal_elem in root.iter('animal'):
            animal_name = animal_elem.get('name')
            animal_data[animal_name] = {}

def menu():
    load_from_xml()  # Load data from XML file
    while True:
        print("Menu:")
        print("1. Print Animal Names")
        print("2. Add Animal Name")
        print("3. Delete Animal Data")
        print("4. Search Animal Data")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        if choice == MenuOptions.PRINT.value:
            printdata()
        if choice == MenuOptions.ADD.value:
            add()
        if choice == MenuOptions.DELETE.value:
            # Implement the delete functionality
            pass
        if choice == MenuOptions.SEARCH.value:
            # Implement the search functionality
            pass
        if choice == MenuOptions.EXIT.value:
            save_to_xml()
            print("Data saved to XML.")
            print("Exiting the program.")
            return

if __name__ == '__main__':
    menu()
