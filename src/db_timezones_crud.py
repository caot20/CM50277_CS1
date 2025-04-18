from src.db_handler import get_connection
from src import utils as u

def validate_insert_input(timezone, utc_offset):
    """
    Validate the user input fields to make 
    sure all the values are as expected.

    Args:
        timezone: String representation of the timezone (IE Europe/London)
        utc_offset: UTC Offset of the timezone (IE 1.0)
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_string(timezone, 3):
        errors.append("timezone must be 3 or more characters in length")
    if not u.validate_offset(utc_offset):
        errors.append("Offset must be between -12.0 and 14.0")

    return errors, timezone, utc_offset

def validate_update_input(timezone_id, timezone, utc_offset):
    """
    Validate the user input fields to make 
    sure all the values are as expected.

    Args:
        timezone_id: Timezone ID representation of the timezone (IE 7 for Europe/London)
        timezone: String representation of the timezone (IE Europe/London)
        utc_offset: UTC Offset of the timezone (IE 1.0)
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(timezone_id, 1, 999):
        errors.append("Timezone ID must be between 1 and 999")
    if not u.validate_string(timezone, 3):
        errors.append("timezone must be 3 or more characters in length")
    if not u.validate_offset(utc_offset):
        errors.append("Offset must be between -12.0 and 14.0")

    return errors, timezone_id, timezone, utc_offset

def validate_get_timezone_input(timezone_id):
    """
    Validate the user input to make 
    sure the value is as expected.

    Args:
        timezone_id: The Numeric Timezone value (IE 1)
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_offset(timezone_id):
        errors.append("Timezone ID must be between 1 and 999")

    return errors, timezone_id

def prompt_insert_input():
    """
    Ask the user for input values so we can validate 
    and then insert/update.
    """
    print("\nEnter the Timzone (Leave blank to leave)")
    timezone = input("Timezone (IE Europe/London): ")
    if not print:
        return None
    
    utc_offset = input("\nEnter The UTC Offset of the Timezone (IE 1.0): ").strip()

    errors \
    , validated_timezone \
    , validated_utc_offset = validate_insert_input( timezone=timezone
                                                  , utc_offset=utc_offset
                                                  )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_timezone \
           , validated_utc_offset

def prompt_update_input():
    """
    Ask the user for input values so we can validate 
    and then insert/update.
    """
    print("\nEnter the Timzone (Leave blank to leave)")
    timezone_id = input("Timezone ID (IE 7 for Europe/London): ")
    if not timezone_id:
        return None

    timezone = input("Timezone (IE Europe/London): ")
    if not print:
        return None    
    
    utc_offset = input("Enter The UTC Offset of the Timezone (IE 1.0): ").strip()

    errors \
    , validated_timezone_id \
    , validated_timezone \
    , validated_utc_offset = validate_update_input(timezone_id=timezone_id
                                                   , timezone=timezone
                                                   , utc_offset=utc_offset
                                                  )
    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_timezone_id \
         , validated_timezone \
         , validated_utc_offset

def prompt_get_timezone_input():
    """
    Ask the user for input value so we can validate 
    and then return data.
    """
    print("\nEnter the Timezone ID (Leave blank to leave)")
    timezone_id = input("Timezone ID (IE 1): ")
    if not timezone_id:
        return None
    
    errors , validated_timezone_id = validate_get_timezone_input(timezone_id=timezone_id)

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_timezone_id 

def create_timezone(timezone, utc_offset):
    """
    Creates a new Timezone (see pytz for common timezones)
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO timezones (timezone, utc_offset) VALUES (?, ?) ON CONFLICT DO NOTHING", (timezone, utc_offset))
        db_connection.commit()
        return db_cursor.lastrowid
            
def get_timezones():
    """
    Return all timezones
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT timezone_id, timezone, utc_offset FROM timezones ORDER BY timezone ASC")
        db_connection.commit()
        return db_cursor.fetchall()

def get_timezone(timezone_id):
    """
    Return a single timezone but as an array for formatting.
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT timezone_id, timezone, utc_offset FROM timezones WHERE timezone_id = ?", (timezone_id,))
        db_connection.commit()
        return db_cursor.fetchall()
    
def update_timezone(timezone_id, timezone, utc_offset):
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("UPDATE timezones SET timezone = ?, utc_offset = ? WHERE timezone_id = ?", (timezone, utc_offset, timezone_id))

        if db_cursor.rowcount == 0:
            print(f"No Timezone ID found with for {timezone_id} ({timezone})")
        else:
            print(f"Updated Timezone ID '{timezone_id}', timezone = '{timezone}' and utc_offset = '{utc_offset}'")
        
        db_connection.commit()

def delete_timezone(timezone_id):
    """
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DELETE FROM timezones WHERE timezone_id = ?", (timezone_id,))

        if db_cursor.rowcount == 0:
            print(f"No Timezone ID found with for {timezone_id}")
        else:
            print(f"Deleted Timezone ID '{timezone_id}'")

        db_connection.commit()
        return timezone_id
