from sys import exit
from src import db_handler as h
from src import menu_countries as menu_c
from src import menu_timezones as menu_t
from src import menu_pilots as menu_p
from src import menu_destinations as menu_d
from src import menu_flights as menu_f
from src import utils as u

def main_menu_options():
    """
    """
    return {
        "1": ("Countries Submenu", countries),
        "2": ("Timezones Submenu", timezones),
        "3": ("Pilots Submenu", pilots),
        "4": ("Destinations Submenu", destinations),
        "5": ("Flights Submenu", flights),
        "9": ("Seed Tables", seed_tables),
        "0": ("Exit", exit_program)
    }

def main_menu():
    """
    Main Menu
    """
    u.clear_screen()
    options = main_menu_options()
    while True:
        print("\n===== Main Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")

def countries():
    """
    Display the Countries Menu
    """
    u.clear_screen()
    options = menu_c.countries_menu_options()
    while True:
        print("\n===== Countries Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")

def timezones():
    """
    Display the Timezone Menu
    """
    u.clear_screen()
    options = menu_t.timezones_menu_options()
    while True:
        print("\n===== Timezones Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")

def pilots():
    """
    Display the Pilots Menu
    """
    u.clear_screen()
    options = menu_p.pilots_menu_options()
    while True:
        print("\n===== Pilots Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")

def destinations():
    """
    Display the Destinations Menu
    """
    u.clear_screen()
    options = menu_d.destinations_menu_options()
    while True:
        print("\n===== Destinations Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")

def flights():
    """
    Display the Flights Menu
    """
    u.clear_screen()
    options = menu_f.flights_menu_options()
    while True:
        print("\n===== Flights Menu =====")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")

        choice = input("Select an option: ").strip().lower()
        action = options.get(choice)

        if action:
            action[1]()
        else:
            print(f"Invalid choice of {choice}, please enter a valid number.")            

def seed_tables():
    """
    Seed Tables
    """
    h.seed_tables()
    print("Tables Seeded")
    

def exit_program():
    print("You have selected 0: Exit")
    print("Goodbye!")
    exit(0)
