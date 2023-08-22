
#Import

from enum import Enum      
import csv # imports from outer csv file
import os

#Enum

class Actions(Enum):
    PRINT = 0
    ADD = 1
    UPDATE = 2  # New option for updating old information
    DELETE = 3
    SEARCH = 4
    EXIT = 5
    INFO = 6  # New option for displaying information


#Arry

cars = [] #this is ther arry who will get all the information from the input
next_car_id = 1  # Initialize the next car ID

#Functions

def print_colored_text(text, color_code): #this function colors the text in terminal in green
    color_start = "\033[" + color_code + "m"
    color_end = "\033[0m"
    colored_text = color_start + text + color_end
    print(colored_text)

def display_info(): # this function shows information about my data
    num_rows = len(cars)  # Number of rows in the 'cars' array
    print(f"Number of rows in 'cars' array: {num_rows}")

def print_car(car): # this function prints after screen clear
    car_info = f"ID: {car['id']}, Name: {car['name']}, Color: {car['color']}, Year: {car['year']}"
    print_colored_text(car_info, "32")  # Print in green


def clear_screen(): # this function clears the screen 
    os.system('cls' if os.name == 'nt' else 'clear' )
    

def update_car(): #this function allows you to update an already given input and change the data
    car = find_car()
    if car is not None:
        car["color"] = input("Enter updated color: ")
        car["year"] = input("Enter updated year: ")
        print("Car updated:", car)
    else:
        print("No such car to update")


def display_menu():      # this function shows the  the menu on terminal,asks for an int input and directs to the right option when you type a number
    for x in Actions:
        print(f'{x.value} - {x.name}')
    return Actions(int(input("Your selection: ")))

def del_car():   #this function uses the find_car function to go on with the program,if the function does find the car it removes it from the arry,else it notifies you there isnt such car
    car = find_car()
    if car is not None:
        cars.remove(car)
        print("Deleted:", car)
    else:
        print("No such car")

def find_car(): # this function takes the search variable and makes worth the input that was given by the user,then the function goes through the arry and compares the input to the data in the arry,if there is a match the program prints the name of the car,if not found it notifies you there isnt such a car
    search = input("Give me a name to search: ")
    for car in cars:
        if car["name"] == search:
            return car
    print("Car not found")
    return None

def save_to_csv(): # this function saves a CSV file
    with open("cars.csv", mode="w", newline="") as file:
        fieldnames = ["id", "color", "year", "name"]  # Include 'id' in fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cars)

def load_from_csv():
    global next_car_id
    try:
        with open("cars.csv", mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                cars.append({
                    "id": int(row["id"]),  # Convert the ID to int
                    "color": row["color"],
                    "year": row["year"],
                    "name": row["name"]
                })
                next_car_id = max(next_car_id, int(row["id"]) + 1)  # Update next_car_id
    except FileNotFoundError:
        pass


def menu(): #this function operates the menu, first it loads infromation to the program from a csv file and then worls a while loop until you stop it
 
    load_from_csv()  # Load data from CSV file at the beginning
    while True: #loop
      
        user_selection = display_menu() # user selects an option on the menu 
        clear_screen()
        if user_selection == Actions.PRINT:
            for car in cars:
                print_car(car)  # Print each car's details
    
       
        if user_selection == Actions.ADD: # Handle the add action and give id
             global next_car_id
             cars.append({
             "id": next_car_id,
             "color": input("Please enter the color: "),
             "year": input("Enter year built: "),
             "name": input("Enter car name: ")
             })
             next_car_id += 1  # Increment the ID for the next car
    
            
     
        if user_selection == Actions.UPDATE:  # Handle the UPDATE action
            update_car()
     
        if user_selection == Actions.DELETE:  # Handle the delete action
            del_car()
     
        if user_selection == Actions.SEARCH:  # handle the search action 
            found_car = find_car()
            if found_car:
                print("Found car:", found_car)

        if user_selection == Actions.INFO:  # Handle the INFO option
            display_info()        
     
        if user_selection == Actions.EXIT:  #Handle the exit action
            save_to_csv()  # Save the data to CSV before exiting
            return       
          
        print(f"Your selection is: {Actions(user_selection).name}") #this order prints your selection 

        
# Entry point 
if __name__ == '__main__': #this is the entry point 
    menu() # this is the program running 
  
        