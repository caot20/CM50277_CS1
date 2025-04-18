from src import db_pilots_crud as p
from src import menus as m

def pilots_menu_options():
    """
    """
    return {
        "1": ("Display Pilots", display_pilots),
        "2": ("Display Pilot", display_pilot),
        "3": ("Create Pilot", create_pilot),
        "4": ("Update Pilot", update_pilot),
        "5": ("Delete Pilot", delete_pilot),
        "0": ("Back", m.main_menu)
    }

def display_pilots():
    """
    Display all the Pilots.
    """
    rows = p.get_pilots()
    if rows:
        print_pilots(rows=rows)
    else:
        print("Query returned no results.")

def display_pilot():
    """
    Display a single Pilot.
    """
    while True:
        data = p.prompt_get_pilot_input()
        if data is None:
            print("Exiting Display Pilots...")
            break

        validated_pilot_id = data

        rows = p.get_pilot(pilot_id=validated_pilot_id)
        if rows:
            print_pilots(rows=rows)
        else:
            print("Query returned no results.")

        see_more = input("\nDisplay another Pilot? (y/n): ").strip().lower()
        if see_more != 'y':
            print("Exiting Display Pilots...")
            break

def print_pilots(rows):
    """
    Print out results to console in a Table Like Output with Fixed Width
    """
    print(f"| {'pilot_id':<9} | {'position (id)':<20} | {'name':<30} | {'passport_number':<15} | {'nationality':<15} |")
    print('-' * 105)
    for row in rows:
        print(f"| {row[0]:<9} | {row[1]:<20} | {row[2]:<30} | {row[3]:<15} | {row[4]:<15} |")
        

def create_pilot():
    """
    Validate and Create a Pilot
    """
    while True:
        data = p.prompt_insert_input()
        if data is None:
            print("Exiting Create Pilot...")
            break

        validated_pilot_position_id \
        , validated_pilot_name \
        , validated_pilot_passport_number \
        , validated_pilot_nationality = data

        pilot_id = p.create_pilot(pilot_position_id=validated_pilot_position_id
                                  , name=validated_pilot_name
                                  , passport_number=validated_pilot_passport_number
                                  , nationality=validated_pilot_nationality
                                 )
        if pilot_id > 0:
            print(f"Added Pilot '{validated_pilot_name} ({validated_pilot_passport_number})' with new pilot_id created as '{pilot_id}'")
        else:
            print(f"Pilot '{validated_pilot_name} ({validated_pilot_passport_number})' not created")

        add_more = input("\nAdd another Pilot? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Create Pilot...")
            break

def update_pilot():
    """
    Validate and Update a Pilot
    """
    while True:
        data = p.prompt_update_input()
        if data is None:
            print("Exiting Update Pilot...")
            break

        validated_pilot_id \
           , validated_pilot_position_id \
           , validated_pilot_name \
           , validated_pilot_passport_number \
           , validated_pilot_nationality = data

        p.update_pilot(pilot_id=validated_pilot_id
                       , pilot_position_id=validated_pilot_position_id
                       , name=validated_pilot_name
                       , passport_number=validated_pilot_passport_number
                       , nationality=validated_pilot_nationality
                      )
        add_more = input("\nUpdate another Pilot? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Update Pilot...")
            break

def delete_pilot():
    """
    Validate and Delete a Pilot
    """
    while True:
        data = p.prompt_get_pilot_input()
        if data is None:
            print("Exiting Delete Pilots...")
            break

        validated_pilot_id = data

        p.delete_pilot(pilot_id=validated_pilot_id)

        delete_more = input("\nDelete another Pilot? (y/n): ").strip().lower()
        if delete_more != 'y':
            print("Exiting Delete Pilots...")
            break
