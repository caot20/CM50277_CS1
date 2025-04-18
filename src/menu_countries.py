from src import db_countries_crud as c
from src import menus as m

def countries_menu_options():
    """
    """
    return {
        "1": ("Display Countries", display_countries),
        "2": ("Display Country by id", display_country),
        "3": ("Create Country", create_country),
        "4": ("Update Country", update_country),
        "5": ("Delete Country", delete_country),
        "0": ("Back", m.main_menu)
    }

def display_countries():
    """
    Display all the countries.
    """
    rows = c.get_countries()
    if rows:
        print_countries(rows=rows)
    else:
        print("Query returned no results.")

def display_country():
    """
    Display a single country.
    """
    while True:
        data = c.prompt_get_country_input()
        if data is None:
            print("Exiting Display Country...")
            break

        validated_country_code_id = data

        rows = c.get_country(country_code_id=validated_country_code_id)
        if rows:
            print_countries(rows=rows)
        else:
            print("Query returned no results.")

        see_more = input("\nDisplay another Country? (y/n): ").strip().lower()
        if see_more != 'y':
            print("Exiting Display Country...")
            break

def print_countries(rows):
    """
    Print out results to console in a Table Like Output with Fixed Width
    """
    print(f"| {'Country Code ID':<15} | {'Alpha-2':<7} | {'Alpha-3':<7} | {'Country':<60} |")
    print('-' * 102)
    for row in rows:
        print(f"| {row[0]:<15} | {row[1]:<7} | {row[2]:<7} | {row[3]:<60} |")

def create_country():
    """
    Validate and Create a country
    """
    while True:
        data = c.prompt_input()
        if data is None:
            print("Exiting Create Country...")
            break

        validated_country_code_id \
           , validated_alpha_2 \
           , validated_alpha_3 \
           , validated_country = data

        c.create_country(validated_country_code_id
                         , validated_alpha_2
                         , validated_alpha_3
                         , validated_country
                         )
        add_more = input("\nAdd another Country? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Create Country...")
            break

def update_country():
    """
    Validate and Update a country
    """
    while True:
        data = c.prompt_input()
        if data is None:
            print("Exiting Update Country...")
            break

        validated_country_code_id \
           , validated_alpha_2 \
           , validated_alpha_3 \
           , validated_country = data

        c.update_country(validated_country_code_id
                         , validated_alpha_2
                         , validated_alpha_3
                         , validated_country
                         )
        add_more = input("\nUpdate another Country? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Update Country...")
            break

def delete_country():
    """
    Validate and Delete a country
    """
    while True:
        data = c.prompt_get_country_input()
        if data is None:
            print("Exiting Delete Country...")
            break

        validated_country_code_id = data

        c.delete_country(country_code_id=validated_country_code_id)

        delete_more = input("\nDelete another Country? (y/n): ").strip().lower()
        if delete_more != 'y':
            print("Exiting Delete Country...")
            break