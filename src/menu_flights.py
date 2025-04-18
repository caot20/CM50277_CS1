from src import db_flights_crud as f
from src import menus as m

def flights_menu_options():
    """
    """
    return {
        "1": ("Display Flights", display_flights),
        "2": ("Display Flight", display_flight),
        "3": ("Create Flights", create_flight),
        "4": ("Update Flights", update_flight),
        "5": ("Delete Flights", delete_flight),
        "0": ("Back", m.main_menu)
    }

def display_flights():
    """
    Display all FUTURE flights.
    """
    rows = f.get_flights()
    if rows:
        print_flights(rows=rows)
    else:
        print("Query returned no results.")

def display_flight():
    """
    Display a single flight in the past or future.
    """
    while True:
        data = f.prompt_get_flight_input()
        if data is None:
            print("Exiting Display Flights...")
            break

        validated_flight_id = data

        rows = f.get_flight(flight_id=validated_flight_id)
        if rows:
            print_flights(rows=rows)
        else:
            print("Query returned no results.")

        see_more = input("\nDisplay another Flight? (y/n): ").strip().lower()
        if see_more != 'y':
            print("Exiting Display Flights...")
            break

def print_flights(rows):
    """
    Print out results to console in a Table Like Output with Fixed Width
    """
    print(f"| {'flight_id':<10} | {'flight_number':<13} | {'origin (a2|id)':<14} | {'origin_departure_utc':<20} | {'dest (a2|id)':<14} | {'dest_arrival_utc':<19} | {'pilot_1 (Rank|Pilot Id)':<40} | {'pilot_2 (Rank|Pilot Id)':<40} |")
    print('-' * 195)
    for row in rows:
        print(f"| {row[0]:<10} | {row[1]:<13} | {row[2]:<14} | {row[3]:<20} | {row[4]:<14} | {row[5]:<19} | {row[6]:<40} | {row[7]:<40} |")
        

def create_flight():
    """
    Validate and Create a Flight
    """
    while True:
        data = f.prompt_insert_input()
        if data is None:
            print("Exiting Create Pilot...")
            break

        validated_flight_number \
         , validated_origin_id \
         , validated_origin_scheduled_departure_time_utc \
         , validated_destination_id \
         , validated_destination_scheduled_arrival_time_utc \
         , validated_scheduled_pilot_1 \
         , validated_scheduled_pilot_2 = data

        flight_id = f.create_flight( flight_number=validated_flight_number
                                   , origin_id=validated_origin_id
                                   , origin_scheduled_departure_time_utc=validated_origin_scheduled_departure_time_utc
                                   , destination_id=validated_destination_id
                                   , destination_scheduled_arrival_time_utc=validated_destination_scheduled_arrival_time_utc
                                   , scheduled_pilot_1=validated_scheduled_pilot_1
                                   , scheduled_pilot_2=validated_scheduled_pilot_2
                                   )
        if flight_id > 0:
            print(f"""
                  ADDED New Flight
                  flight_number: {validated_flight_number}
                  origin_id: {validated_origin_id}
                  origin_scheduled_departure_time_utc: {validated_origin_scheduled_departure_time_utc}
                  destination_id: {validated_destination_id}
                  destination_scheduled_arrival_time_ut: {validated_destination_scheduled_arrival_time_utc}
                  scheduled_pilot_1: {validated_scheduled_pilot_1}
                  scheduled_pilot_2: {validated_scheduled_pilot_2}
                  """
                  )
        else:
            print(f"Flight '{validated_flight_number} ({validated_origin_id}/{validated_destination_id})' not created")

        add_more = input("\nAdd another Flight? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Create Flight...")
            break

def update_flight():
    """
    Validate and Update a Flight
    """
    while True:
        data = f.prompt_update_input()
        if data is None:
            print("Exiting Update Flight...")
            break

        validated_flight_id \
        , alidated_flight_number \
        , validated_origin_id \
        , validated_origin_scheduled_departure_time_utc \
        , validated_destination_id \
        , validated_destination_scheduled_arrival_time_utc \
        , validated_scheduled_pilot_1 \
        , validated_scheduled_pilot_2 = data

        f.update_flight( flight_id=validated_flight_id
                       , flight_number=alidated_flight_number
                       , origin_id=validated_origin_id
                       , origin_scheduled_departure_time_utc=validated_origin_scheduled_departure_time_utc
                       , destination_id=validated_destination_id
                       , destination_scheduled_arrival_time_utc=validated_destination_scheduled_arrival_time_utc
                       , scheduled_pilot_1=validated_scheduled_pilot_1
                       , scheduled_pilot_2=validated_scheduled_pilot_2
                      )
        add_more = input("\nUpdate another Flight? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Update Flights...")
            break

def delete_flight():
    """
    Validate and Delete a Flight
    """
    while True:
        data = f.prompt_get_flight_input()
        if data is None:
            print("Exiting Delete Flights...")
            break

        validated_flight_id = data

        f.delete_flight(flight_id=validated_flight_id)

        delete_more = input("\nDelete another Flight? (y/n): ").strip().lower()
        if delete_more != 'y':
            print("Exiting Delete Flights...")
            break
