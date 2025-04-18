from src import db_destinations_crud as d
from src import menus as m

def destinations_menu_options():
    """
    """
    return {
        "1": ("Display Destinations", display_destinations),
        "2": ("Display Destination", display_destination),
        "3": ("Create Destinations", create_destination),
        "4": ("Update Destinations", update_destination),
        "5": ("Delete Destinations", delete_destination),
        "0": ("Back", m.main_menu)
    }

def display_destinations():
    """
    Display all the Destinations.
    """
    rows = d.get_destinations()
    if rows:
        print_destinations(rows=rows)
    else:
        print("Query returned no results.")

def display_destination():
    """
    Display a single Destination.
    """
    while True:
        data = d.prompt_get_destination_input()
        if data is None:
            print("Exiting Display Destinations...")
            break

        validated_destination_id = data

        rows = d.get_destination(destination_id=validated_destination_id)
        if rows:
            print_destinations(rows=rows)
        else:
            print("Query returned no results.")

        see_more = input("\nDisplay another Destination? (y/n): ").strip().lower()
        if see_more != 'y':
            print("Exiting Display Destinationss...")
            break

def print_destinations(rows):
    """
    Print out results to console in a Table Like Output with Fixed Width
    """
    print(f"| {'destination_id':<14} | {'iata_code':<9} | {'icao_code':<9} | {'latitude':<11} | {'longitude':<11} | {'description':<40} | {'area':<20} | {'timezone (offset|id)':<30} | {'country (Alpha-2)':<25} |")
    print('-' * 197)
    for row in rows:
        print(f"| {row[0]:<14} | {row[1]:<9} | {row[2]:<9} | {row[3]:<11} | {row[4]:<11} | {row[5]:<40} | {row[6]:<20} | {row[7]:<30} | {row[8]:<25} |")
        

def create_destination():
    """
    Validate and Create a Destination
    """
    while True:
        data = d.prompt_insert_input()
        if data is None:
            print("Exiting Create Pilot...")
            break

        validated_iata_code \
        , validated_icao_code \
        , validated_latitude \
        , validated_longitude \
        , validated_description \
        , validated_area \
        , validated_timezone_id \
        , validated_country_code_id = data

        pilot_id = d.create_destination(iata_code=validated_iata_code
                                        , icao_code=validated_icao_code
                                        , latitude=validated_latitude
                                        , longitude=validated_longitude
                                        , description=validated_description
                                        , area=validated_area
                                        , timezone_id=validated_timezone_id
                                        , country_code_id=validated_country_code_id
                                       )
        if pilot_id > 0:
            print(f"""
                  ADDED New Destination
                  iata_code: {validated_iata_code}
                  icao_code: {validated_icao_code}
                  latitude: {validated_latitude}
                  longitude: {validated_longitude}
                  description: {validated_description}
                  area: {validated_area}
                  timezone_id: {validated_timezone_id}
                  country_code_id: {validated_country_code_id}
                  """
                  )
        else:
            print(f"Destination '{validated_iata_code} ({validated_icao_code})' not created")

        add_more = input("\nAdd another Destination? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Create Destination...")
            break

def update_destination():
    """
    Validate and Update a Destination
    """
    while True:
        data = d.prompt_update_input()
        if data is None:
            print("Exiting Update Pilot...")
            break

        validated_destination_id \
        , validated_iata_code \
        , validated_icao_code \
        , validated_latitude \
        , validated_longitude \
        , validated_description \
        , validated_area \
        , validated_timezone_id \
        , validated_country_code_id = data

        d.update_destination(destination_id=validated_destination_id
                            , iata_code=validated_iata_code
                            , icao_code=validated_icao_code
                            , latitude=validated_latitude
                            , longitude=validated_longitude
                            , description=validated_description
                            , area=validated_area
                            , timezone_id=validated_timezone_id
                            , country_code_id=validated_country_code_id
                      )
        add_more = input("\nUpdate another Destination? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Update Destinations...")
            break

def delete_destination():
    """
    Validate and Delete a Destination
    """
    while True:
        data = d.prompt_get_destination_input()
        if data is None:
            print("Exiting Delete Destinations...")
            break

        validated_destination_id = data

        d.delete_destination(destination_id=validated_destination_id)

        delete_more = input("\nDelete another Destination? (y/n): ").strip().lower()
        if delete_more != 'y':
            print("Exiting Delete Destinations...")
            break
