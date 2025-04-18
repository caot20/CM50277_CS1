from src.db_handler import get_connection
from src import utils as u
from datetime import datetime, timedelta

def validate_insert_input( flight_number
                         , origin_id
                         , origin_scheduled_departure_time_utc
                         , destination_id
                         , destination_scheduled_arrival_time_utc
                         , scheduled_pilot_1
                         , scheduled_pilot_2
                         ):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        flight_number:
        origin_id:
        origin_scheduled_departure_time_utc:
        destination_id:
        destination_scheduled_arrival_time_utc:
        scheduled_pilot_1:
        scheduled_pilot_2:
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_string(flight_number, 5):
        errors.append("flight_number must be 5 or more characters in length")
    if not u.validate_int(origin_id, 1, 999):
        errors.append("origin_id must be between 1 and 999")
    if not u.validate_iso8601(origin_scheduled_departure_time_utc):
        errors.append("origin_scheduled_departure_time_utc must be a valid ISO 8601 Date")
    if not u.validate_int(destination_id, 1, 999):
        errors.append("destination_id must be between 1 and 999")
    if not u.validate_iso8601(destination_scheduled_arrival_time_utc):
        errors.append("destination_scheduled_arrival_time_utc must be a valid ISO 8601 Date")        
    if not u.validate_int(scheduled_pilot_1, 1, 999):
        errors.append("scheduled_pilot_1 must be between 1 and 999")
    if not u.validate_int(scheduled_pilot_2, 1, 999):
        errors.append("scheduled_pilot_2 must be between 1 and 999")

    return errors \
         , flight_number \
         , origin_id \
         , origin_scheduled_departure_time_utc \
         , destination_id \
         , destination_scheduled_arrival_time_utc \
         , scheduled_pilot_1 \
         , scheduled_pilot_2

def validate_update_input( flight_id
                         , flight_number
                         , origin_id
                         , origin_scheduled_departure_time_utc
                         , destination_id
                         , destination_scheduled_arrival_time_utc
                         , scheduled_pilot_1
                         , scheduled_pilot_2
                         ):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        flight_id:
        flight_number:
        origin_id:
        origin_scheduled_departure_time_utc:
        destination_id:
        destination_scheduled_arrival_time_utc:
        scheduled_pilot_1:
        scheduled_pilot_2:
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(flight_id, 1, 999):
        errors.append("flight_id must be between 1 and 999")
    if not u.validate_string(flight_number, 5):
        errors.append("flight_number must be 5 or more characters in length")
    if not u.validate_int(origin_id, 1, 999):
        errors.append("origin_id must be between 1 and 999")
    if not u.validate_iso8601(origin_scheduled_departure_time_utc):
        errors.append("origin_scheduled_departure_time_utc must be a valid ISO 8601 Date")
    if not u.validate_int(destination_id, 1, 999):
        errors.append("destination_id must be between 1 and 999")
    if not u.validate_iso8601(destination_scheduled_arrival_time_utc):
        errors.append("destination_scheduled_arrival_time_utc must be a valid ISO 8601 Date")        
    if not u.validate_int(scheduled_pilot_1, 1, 999):
        errors.append("scheduled_pilot_1 must be between 1 and 999")
    if not u.validate_int(scheduled_pilot_2, 1, 999):
        errors.append("scheduled_pilot_2 must be between 1 and 999")

    return errors \
         , flight_id \
         , flight_number \
         , origin_id \
         , origin_scheduled_departure_time_utc \
         , destination_id \
         , destination_scheduled_arrival_time_utc \
         , scheduled_pilot_1 \
         , scheduled_pilot_2

def validate_get_flight_input(flight_id):
    """
    Validate the user input to make
    sure the value is as expected.

    Args:
        flight_id: id of the flight record.
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(flight_id, 1, 999):
        errors.append("Flight ID must be between 1 and 999")

    return errors, flight_id

def prompt_insert_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("Enter Flight Information")

    flight_number = input("Enter Flight Number, Leave blank to leave): ")
    if not flight_number:
        return None

    origin_id = input("Enter the Origin ID (destination_id): ").strip()
    origin_scheduled_departure_time_utc = input(f"Enter Scheduled Departure time in UTC ISO 8601, e.g., {datetime.now().isoformat()}: ").strip()
    destination_id = input("Enter the Destination ID: ").strip()
    destination_scheduled_arrival_time_utc = input(f"Enter Scheduled Arrival time in UTC ISO 8601, e.g., {(datetime.now() + timedelta(minutes=60)).isoformat()}: ").strip()
    scheduled_pilot_1 = input("Enter Pilot 1 ID: ").strip()
    scheduled_pilot_2 = input("Enter Pilot 2 ID: ").strip()
    
    errors \
    , validated_flight_number \
    , validated_origin_id \
    , validated_origin_scheduled_departure_time_utc \
    , validated_destination_id \
    , validated_destination_scheduled_arrival_time_utc \
    , validated_scheduled_pilot_1 \
    , validated_scheduled_pilot_2 = validate_insert_input(flight_number
                                                         , origin_id
                                                         , origin_scheduled_departure_time_utc
                                                         , destination_id
                                                         , destination_scheduled_arrival_time_utc
                                                         , scheduled_pilot_1
                                                         , scheduled_pilot_2
                                                         )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_flight_number \
         , validated_origin_id \
         , validated_origin_scheduled_departure_time_utc \
         , validated_destination_id \
         , validated_destination_scheduled_arrival_time_utc \
         , validated_scheduled_pilot_1 \
         , validated_scheduled_pilot_2

def prompt_update_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("Enter Flight Information")

    flight_id = input("Enter Flight ID, Leave blank to leave): ")
    if not flight_id:
        return None
    
    flight_number = input("Enter Flight Number: ")
    origin_id = input("Enter the Origin ID (destination_id): ").strip()
    origin_scheduled_departure_time_utc = input(f"Enter Scheduled Departure time in UTC ISO 8601, e.g., {datetime.now().isoformat()}: ").strip()
    destination_id = input("Enter the Destination ID: ").strip()
    destination_scheduled_arrival_time_utc = input(f"Enter Scheduled Arrival time in UTC ISO 8601, e.g., {datetime.now().isoformat()}: ").strip()
    scheduled_pilot_1 = input("Enter Pilot 1 ID: ").strip()
    scheduled_pilot_2 = input("Enter Pilot 2 ID: ").strip()
    
    errors \
    , validated_flight_id \
    , validated_flight_number \
    , validated_origin_id \
    , validated_origin_scheduled_departure_time_utc \
    , validated_destination_id \
    , validated_destination_scheduled_arrival_time_utc \
    , validated_scheduled_pilot_1 \
    , validated_scheduled_pilot_2 = validate_update_input(flight_id=flight_id
                                                         , flight_number=flight_number
                                                         , origin_id=origin_id
                                                         , origin_scheduled_departure_time_utc=origin_scheduled_departure_time_utc
                                                         , destination_id=destination_id
                                                         , destination_scheduled_arrival_time_utc=destination_scheduled_arrival_time_utc
                                                         , scheduled_pilot_1=scheduled_pilot_1
                                                         , scheduled_pilot_2=scheduled_pilot_2
                                                         )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_flight_id \
         , validated_flight_number \
         , validated_origin_id \
         , validated_origin_scheduled_departure_time_utc \
         , validated_destination_id \
         , validated_destination_scheduled_arrival_time_utc \
         , validated_scheduled_pilot_1 \
         , validated_scheduled_pilot_2

def prompt_get_flight_input():
    """
    Ask the user for input value so we can validate
    and then return data.
    """
    print("Enter the Flight ID (Leave blank to leave)")
    flight_id = input("Flight ID (IE 1): ")
    if not flight_id:
        return None

    errors , validated_flight_id = validate_get_flight_input(flight_id=flight_id)

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_flight_id

def create_flight( flight_number
                 , origin_id
                 , origin_scheduled_departure_time_utc
                 , destination_id
                 , destination_scheduled_arrival_time_utc
                 , scheduled_pilot_1
                 , scheduled_pilot_2
                 ):
    """
    Creates a new Flight
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          INSERT INTO flights (flight_number, 
                                               origin_id,
                                               origin_scheduled_departure_time_utc, 
                                               destination_id, 
                                               destination_scheduled_arrival_time_utc, 
                                               scheduled_pilot_1, 
                                               scheduled_pilot_2
                                               ) 
                          VALUES (?, ?, ?, ?, ?, ?, ?) 
                          """, ( flight_number
                               , origin_id
                               , origin_scheduled_departure_time_utc
                               , destination_id
                               , destination_scheduled_arrival_time_utc
                               , scheduled_pilot_1
                               , scheduled_pilot_2
                               ))
        db_connection.commit()
        return db_cursor.lastrowid

def get_flights():
    """
    Return all FUTURE flights
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT flight_id,
                          flight_number,
                          o.icao_code || ' (' || o.iata_code || '|' || o.destination_id || ')' AS origin,
                          f.origin_scheduled_departure_time_utc AS origin_departure_utc,
                          d.icao_code || ' (' || d.iata_code || '|' || d.destination_id || ')' AS destination,
                          f.destination_scheduled_arrival_time_utc AS destination_arrival_utc,
                          p1.name || ' (' || pp1.position || '|' || p1.pilot_id || ')' AS pilot_1,
                          p2.name || ' (' || pp2.position || '|' || p2.pilot_id || ')' AS pilot_2
                          FROM flights AS f
                          LEFT JOIN destinations AS o ON o.destination_id = f.origin_id
                          LEFT JOIN destinations AS d ON d.destination_id = f.destination_id
                          LEFT JOIN pilots AS p1 on p1.pilot_id = f.scheduled_pilot_1
                          LEFT JOIN pilot_positions AS pp1 on pp1.pilot_position_id = p1.pilot_position_id
                          LEFT JOIN pilots AS p2 on p2.pilot_id = f.scheduled_pilot_2
                          LEFT JOIN pilot_positions AS pp2 on pp2.pilot_position_id = p2.pilot_position_id
                          WHERE origin_scheduled_departure_time_utc >= DATETIME('now') ;
                          """)
        db_connection.commit()
        return db_cursor.fetchall()

def get_flight(flight_id):
    """
    Return a single flight
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT flight_id,
                          flight_number,
                          o.icao_code || ' (' || o.iata_code || '|' || o.destination_id || ')' AS origin,
                          f.origin_scheduled_departure_time_utc AS origin_departure_utc,
                          d.icao_code || ' (' || d.iata_code || '|' || d.destination_id || ')' AS destination,
                          f.destination_scheduled_arrival_time_utc AS destination_arrival_utc,
                          p1.name || ' (' || pp1.position || '|' || p1.pilot_id || ')' AS pilot_1,
                          p2.name || ' (' || pp2.position || '|' || p2.pilot_id || ')' AS pilot_2
                          FROM flights AS f
                          LEFT JOIN destinations AS o ON o.destination_id = f.origin_id
                          LEFT JOIN destinations AS d ON d.destination_id = f.destination_id
                          LEFT JOIN pilots AS p1 on p1.pilot_id = f.scheduled_pilot_1
                          LEFT JOIN pilot_positions AS pp1 on pp1.pilot_position_id = p1.pilot_position_id
                          LEFT JOIN pilots AS p2 on p2.pilot_id = f.scheduled_pilot_2
                          LEFT JOIN pilot_positions AS pp2 on pp2.pilot_position_id = p2.pilot_position_id
                          WHERE f.flight_id = ? ;
                          """, (flight_id,))
        db_connection.commit()
        return db_cursor.fetchall()

def update_flight( flight_id 
                 , flight_number
                 , origin_id
                 , origin_scheduled_departure_time_utc
                 , destination_id
                 , destination_scheduled_arrival_time_utc
                 , scheduled_pilot_1 
                 , scheduled_pilot_2
                 ):
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          UPDATE flights 
                          SET flight_number = ?, 
                              origin_id = ?, 
                              origin_scheduled_departure_time_utc = ?, 
                              destination_id = ?,
                              destination_scheduled_arrival_time_utc = ?,
                              scheduled_pilot_1 = ?, 
                              scheduled_pilot_2 = ?
                          WHERE flight_id = ?
                          """
                          , ( flight_number
                            , origin_id
                            , origin_scheduled_departure_time_utc
                            , destination_id
                            , destination_scheduled_arrival_time_utc
                            , scheduled_pilot_1
                            , scheduled_pilot_2
                            , flight_id
                            ))

        if db_cursor.rowcount == 0:
            print(f"No Flight ID found with for {flight_id} ({flight_number} - {origin_id}/{destination_id})")
        else:
            print(f"""
                  UPDATED flight:
                  flight_id: {flight_id}
                  flight_number: {flight_number}
                  origin_id: {origin_id}
                  origin_scheduled_departure_time_utc: {origin_scheduled_departure_time_utc}
                  destination_id: {destination_id}
                  destination_scheduled_arrival_time_utc: {destination_scheduled_arrival_time_utc}
                  scheduled_pilot_1: {scheduled_pilot_1}
                  scheduled_pilot_2: {scheduled_pilot_2}
                  """
                  )

        db_connection.commit()

def delete_flight(flight_id):
    """
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DELETE FROM flights WHERE flight_id = ?", (flight_id,))

        if db_cursor.rowcount == 0:
            print(f"No Flight ID found with for {flight_id}")
        else:
            print(f"Deleted Flight ID '{flight_id}'")

        db_connection.commit()
        return flight_id
