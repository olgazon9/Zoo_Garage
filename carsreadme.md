##Car Management Program
This Python script is designed to manage a list of cars. It provides an interactive console-based menu for various car-related actions.

Imports and Enum
enum.Enum is used to define the Actions enumeration representing different user choices.
The csv module is used to read and write CSV files.
The os module is used to clear the console screen.
 
 Functions

print_colored_text(text, color_code): Prints text in a specified color.
display_info(): Displays information about the number of cars in the list.
print_car(car): Prints car information in a colored format.
clear_screen(): Clears the console screen.
update_car(): Allows updating color and year of an existing car.
display_menu(): Displays the menu and returns user choice.
del_car(): Deletes a car from the list based on user input.
find_car(): Searches for a car by name and returns its dictionary if found.
save_to_csv(): Saves the car list to a CSV file.
load_from_csv(): Loads data from a CSV file into the car list.
menu(): The main function handling the interactive menu.

 Usage
Run the script.
Choose from the menu options to manage car data.
Follow on-screen instructions for each action.

 Note
Data is stored in the cars list as dictionaries.
The program saves and loads data to/from a CSV file named "cars.csv".