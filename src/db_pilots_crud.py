from src.db_handler import get_connection
from src import utils as u

def validate_insert_input(position, name, passport_number, nationality):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        position: String representation of the position (IE Captain)
        name: Name of the pilot (IE Chesley Sullenberger)
        passport_number: Pilots passport number
        nationality: Pilots nationality
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(position, 0, 1):
        errors.append("Position must be 0 or 1 (Captain and First Officer)")
    if not u.validate_string(name, 4):
        errors.append("name must be 4 or more characters in length")
    if not u.validate_string(passport_number, 9):
        errors.append("passport_number must be 9 or more characters in length")
    if not u.validate_string(nationality, 4):
        errors.append("nationality must be 4 or more characters in length")

    return errors, position, name, passport_number, nationality

def validate_update_input(pilot_id, position, name, passport_number, nationality):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        pilot_id: id of the pilot record.
        position: String representation of the position (IE Captain)
        name: Name of the pilot (IE Chesley Sullenberger)
        passport_number: Pilots passport number
        nationality: Pilots nationality
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(pilot_id, 0, 999):
        errors.append("Pilot ID must be between 1 and 999")
    if not u.validate_int(position, 0, 1):
        errors.append("Position must be 0 or 1 (Captain and First Officer)")
    if not u.validate_string(name, 4):
        errors.append("name must be 4 or more characters in length")
    if not u.validate_string(passport_number, 9):
        errors.append("passport_number must be 9 or more characters in length")
    if not u.validate_string(nationality, 4):
        errors.append("nationality must be 4 or more characters in length")

    return errors, pilot_id, position, name, passport_number, nationality

def validate_get_pilot_input(pilot_id):
    """
    Validate the user input to make
    sure the value is as expected.

    Args:
        pilot_id: id of the pilot record.
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(pilot_id, 0, 999):
        errors.append("Pilot ID must be between 1 and 999")

    return errors, pilot_id

def prompt_insert_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("Enter the Pilots Information")
    pilot_position_id = input("Enter the Pilots Position (0 for Captain, 1 for First Officer, Leave blank to leave): ")
    if not pilot_position_id:
        return None

    pilot_name = input("Enter the Pilots Name (IE Amelia Earhart): ").strip()
    pilot_passport_number = input("Enter the Pilots Passport Number (IE GB1234567): ").strip()
    pilot_nationality = input("Enter Pilots Nationality (IE British): ").strip()

    errors \
    , validated_pilot_position_id \
    , validated_pilot_name \
    , validated_pilot_passport_number \
    , validated_pilot_nationality = validate_insert_input( position=pilot_position_id
                                                          , name=pilot_name
                                                          , passport_number=pilot_passport_number
                                                          , nationality=pilot_nationality
                                                          )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_pilot_position_id \
           , validated_pilot_name \
           , validated_pilot_passport_number \
           , validated_pilot_nationality

def prompt_update_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("\nEnter the Pilots Information")
    print("\nEnter the Pilot ID (Leave blank to leave)")
    pilot_id = input("Pilot ID (IE 1): ")
    if not pilot_id:
        return None

    print("Enter the Pilots Position (0 or 1 Leave blank to leave)")
    pilot_position_id = input("Enter the Pilots Position (IE 0 for Captain, 1 for First Officer): ")
    if not pilot_position_id:
        return None

    pilot_name = input("Enter the Pilots Name (IE Amelia Earhart): ").strip()
    pilot_passport_number = input("Enter the Pilots Passport Number (IE GB1234567): ").strip()
    pilot_nationality = input("Enter Pilots Nationality (IE British): ").strip()

    errors \
    , validated_pilot_id \
    , validated_pilot_position_id \
    , validated_pilot_name \
    , validated_pilot_passport_number \
    , validated_pilot_nationality = validate_update_input(pilot_id=pilot_id
                                                          ,position=pilot_position_id
                                                          , name=pilot_name
                                                          , passport_number=pilot_passport_number
                                                          , nationality=pilot_nationality
                                                          )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_pilot_id \
           , validated_pilot_position_id \
           , validated_pilot_name \
           , validated_pilot_passport_number \
           , validated_pilot_nationality

def prompt_get_pilot_input():
    """
    Ask the user for input value so we can validate
    and then return data.
    """
    print("Enter the Pilot ID (Leave blank to leave)")
    pilot_id = input("Pilot ID (IE 1): ")
    if not pilot_id:
        return None

    errors , validated_pilot_id = validate_get_pilot_input(pilot_id=pilot_id)

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_pilot_id

def create_pilot(pilot_position_id, name, passport_number, nationality):
    """
    Creates a new Pilot
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          INSERT INTO pilots (pilot_position_id, name, passport_number, nationality) VALUES (?, ?, ?, ?) ON CONFLICT DO NOTHING""", (pilot_position_id, name, passport_number, nationality))
        db_connection.commit()
        return db_cursor.lastrowid

def get_pilots():
    """
    Return all pilots
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT P.pilot_id,
                          pp.position || ' (' || p.pilot_position_id || ')' AS position,
                          p.name,
                          p.passport_number,
                          p.nationality
                          FROM pilots AS p
                          JOIN pilot_positions as PP on PP.pilot_position_id = P.pilot_position_id;
                          """)
        db_connection.commit()
        return db_cursor.fetchall()

def get_pilot(pilot_id):
    """
    Return all pilots
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT P.pilot_id,
                          pp.position || ' (' || p.pilot_position_id || ')' AS position,
                          p.name,
                          p.passport_number,
                          p.nationality
                          FROM pilots AS p
                          JOIN pilot_positions as PP on PP.pilot_position_id = P.pilot_position_id
                          WHERE pilot_id = ? ;
                          """, (pilot_id,))
        db_connection.commit()
        return db_cursor.fetchall()

def update_pilot(pilot_id, pilot_position_id, name, passport_number, nationality):
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("UPDATE pilots SET pilot_position_id = ?, name = ?, passport_number = ?, nationality = ? WHERE pilot_id = ?", (pilot_position_id, name, passport_number, nationality, pilot_id))

        if db_cursor.rowcount == 0:
            print(f"No Pilot ID found with for {pilot_id} ({passport_number})")
        else:
            print(f"""
                  UPDATED Pilot ID: '{pilot_id}',
                  pilot_position_id: '{pilot_position_id}',
                  name: '{name}',
                  passport_number: '{passport_number}',
                  nationality: '{nationality}'
                  """
                  )

        db_connection.commit()

def delete_pilot(pilot_id):
    """
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DELETE FROM pilots WHERE pilot_id = ?", (pilot_id,))

        if db_cursor.rowcount == 0:
            print(f"No Pilot ID found with for {pilot_id}")
        else:
            print(f"Deleted Pilot ID '{pilot_id}'")

        db_connection.commit()
        return pilot_id
