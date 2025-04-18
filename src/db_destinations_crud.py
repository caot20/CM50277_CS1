from src.db_handler import get_connection
from src import utils as u

def validate_insert_input(iata_code, 
                          icao_code, 
                          latitude, 
                          longitude,
                          description,
                          area,
                          timezone_id,
                          country_code_id
                          ):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        iata_code: 
        icao_code:
        latitude:
        longitude:
        description:
        area:
        timezone_id:
        country_code_id:
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_string(iata_code, 3):
        errors.append("iata_code must be 3 or more characters in length")
    if not u.validate_string(icao_code, 4):
        errors.append("icao_code must be 4 or more characters in length")
    if not u.validate_real(latitude):
        errors.append("latitude must be a real")
    if not u.validate_real(longitude):
        errors.append("longitude must be a real")        
    if not u.validate_string(description, 5):
        errors.append("description must be 5 or more characters in length")        
    if not u.validate_string(area, 5):
        errors.append("area must be 5 or more characters in length")                
    if not u.validate_int(timezone_id, 1, 999):
        errors.append("timezone_id must be between 1 and 999")
    if not u.validate_int(country_code_id, 1, 999):
        errors.append("country_code_id must be between 1 and 999")

    return errors, \
        iata_code, \
        icao_code, \
        latitude, \
        longitude, \
        description, \
        area, \
        timezone_id, \
        country_code_id

def validate_update_input(destination_id
                         , iata_code
                         , icao_code
                         , latitude
                         , longitude
                         , description
                         , area
                         , timezone_id
                         , country_code_id
                         ):
    """
    Validate the user input fields to make
    sure all the values are as expected.

    Args:
        iata_code: 
        icao_code:
        latitude:
        longitude:
        description:
        area:
        timezone_id:
        country_code_id:
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(destination_id, 1, 999):
        errors.append("destination_id must be between 1 and 999")
    if not u.validate_string(iata_code, 3):
        errors.append("iata_code must be 3 or more characters in length")
    if not u.validate_string(icao_code, 4):
        errors.append("icao_code must be 4 or more characters in length")
    if not u.validate_real(latitude):
        errors.append("latitude must be a real")
    if not u.validate_real(longitude):
        errors.append("longitude must be a real")        
    if not u.validate_string(description, 5):
        errors.append("description must be 5 or more characters in length")        
    if not u.validate_string(area, 5):
        errors.append("area must be 5 or more characters in length")                
    if not u.validate_int(timezone_id, 1, 999):
        errors.append("timezone_id must be between 1 and 999")
    if not u.validate_int(country_code_id, 1, 999):
        errors.append("country_code_id must be between 1 and 999")

    return errors, \
        destination_id, \
        iata_code, \
        icao_code, \
        latitude, \
        longitude, \
        description, \
        area, \
        timezone_id, \
        country_code_id

def validate_get_destination_input(destination_id):
    """
    Validate the user input to make
    sure the value is as expected.

    Args:
        destination_id: id of the destination record.
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(destination_id, 0, 999):
        errors.append("Destination ID must be between 1 and 999")

    return errors, destination_id

def prompt_insert_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("Enter Destination Information")

    iata_code = input("Enter the IATA code, Leave blank to leave): ")
    if not iata_code:
        return None

    icao_code = input("Enter the ICAO code: ").strip()
    latitude = input("Enter Latitude coordinates: ").strip()
    longitude = input("Enter Longitude coordinates: ").strip()
    description = input("Enter Description: ").strip()
    area = input("Enter Area: ").strip()
    timezone_id = input("Enter timezone_id: ").strip()
    country_code_id = input("Enter country_code_id: ").strip()
    
    errors \
    , validated_iata_code \
    , validated_icao_code \
    , validated_latitude \
    , validated_longitude \
    , validated_description \
    , validated_area \
    , validated_timezone_id \
    , validated_country_code_id = validate_insert_input(iata_code
                                                        , icao_code
                                                        , latitude
                                                        , longitude
                                                        , description
                                                        , area
                                                        , timezone_id
                                                        , country_code_id
                                                        )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_iata_code \
        , validated_icao_code \
        , validated_latitude \
        , validated_longitude \
        , validated_description \
        , validated_area \
        , validated_timezone_id \
        , validated_country_code_id

def prompt_update_input():
    """
    Ask the user for input values so we can validate
    and then insert/update.
    """
    print("Enter Destination Information")

    destination_id = input("Enter the destination_id, Leave blank to leave): ")
    if not destination_id:
        return None

    iata_code = input("Enter the IATA code: ").strip()
    icao_code = input("Enter the ICAO code: ").strip()
    latitude = input("Enter Latitude coordinates: ").strip()
    longitude = input("Enter Longitude coordinates: ").strip()
    description = input("Enter Description: ").strip()
    area = input("Enter Area: ").strip()
    timezone_id = input("Enter timezone_id: ").strip()
    country_code_id = input("Enter country_code_id: ").strip()
    
    errors \
    , validated_destination_id \
    , validated_iata_code \
    , validated_icao_code \
    , validated_latitude \
    , validated_longitude \
    , validated_description \
    , validated_area \
    , validated_timezone_id \
    , validated_country_code_id = validate_update_input(destination_id=destination_id
                                                        , iata_code=iata_code
                                                        , icao_code=icao_code
                                                        , latitude=latitude
                                                        , longitude=longitude
                                                        , description=description
                                                        , area=area
                                                        , timezone_id=timezone_id
                                                        , country_code_id=country_code_id
                                                        )

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_destination_id \
        , validated_iata_code \
        , validated_icao_code \
        , validated_latitude \
        , validated_longitude \
        , validated_description \
        , validated_area \
        , validated_timezone_id \
        , validated_country_code_id

def prompt_get_destination_input():
    """
    Ask the user for input value so we can validate
    and then return data.
    """
    print("Enter the Destination ID (Leave blank to leave)")
    destination_id = input("Destination ID (IE 1): ")
    if not destination_id:
        return None

    errors , validated_destination_id = validate_get_destination_input(destination_id=destination_id)

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_destination_id

def create_destination(iata_code
                       , icao_code
                       , latitude
                       , longitude
                       , description
                       , area
                       , timezone_id
                       , country_code_id
                       ):
    """
    Creates a new Destination
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          INSERT INTO destinations (iata_code, 
                                                    icao_code, 
                                                    latitude, 
                                                    longitude, 
                                                    description, 
                                                    area, 
                                                    timezone_id, 
                                                    country_code_id
                                                    ) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
                          ON CONFLICT DO NOTHING
                          """, (iata_code
                                , icao_code
                                , latitude
                                , longitude
                                , description
                                , area
                                , timezone_id
                                , country_code_id))
        db_connection.commit()
        return db_cursor.lastrowid

def get_destinations():
    """
    Return all Destinations
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT d.destination_id,
                          d.iata_code,
                          d.icao_code,
                          d.latitude,
                          d.longitude,
                          d.description,
                          d.area,
                          tz.timezone || ' (' || tz.utc_offset || '|' || tz.timezone_id || ')' AS timezone,
                          c.country || ' (' || c.alpha_2 || '|' || c.country_code_id || ')' AS country
                          FROM destinations AS d
                          LEFT JOIN timezones AS tz on tz.timezone_id = d.timezone_id
                          LEFT JOIN countries AS c on c.country_code_id = d.country_code_id ;
                          """)
        db_connection.commit()
        return db_cursor.fetchall()

def get_destination(destination_id):
    """
    Return a single destination
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          SELECT d.destination_id,
                          d.iata_code,
                          d.icao_code,
                          d.latitude,
                          d.longitude,
                          d.description,
                          d.area,
                          tz.timezone || ' (' || tz.utc_offset || '|' || tz.timezone_id || ')' AS timezone,
                          c.country || ' (' || c.alpha_2 || '|' || c.country_code_id || ')' AS country
                          FROM destinations AS d
                          LEFT JOIN timezones AS tz on tz.timezone_id = d.timezone_id
                          LEFT JOIN countries AS c on c.country_code_id = d.country_code_id 
                          WHERE d.destination_id = ?;
                          """, (destination_id,))
        db_connection.commit()
        return db_cursor.fetchall()

def update_destination(destination_id
                      , iata_code
                      , icao_code
                      , latitude
                      , longitude
                      , description
                      , area
                      , timezone_id
                      , country_code_id
                      ):
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""
                          UPDATE destinations 
                          SET iata_code = ?, 
                              icao_code = ?, 
                              latitude = ?, 
                              longitude = ?,
                              description = ?,
                              area = ?, 
                              timezone_id = ?, 
                              country_code_id = ?
                          WHERE destination_id = ?
                          """
                          , (iata_code
                            , icao_code
                            , latitude
                            , longitude
                            , description
                            , area
                            , timezone_id
                            , country_code_id
                            , destination_id
                            ))

        if db_cursor.rowcount == 0:
            print(f"No Destination ID found with for {destination_id} ({iata_code}/{icao_code})")
        else:
            print(f"""
                  UPDATED destinations:
                  destination_id: '{destination_id}'
                  iata_code: '{iata_code}'
                  icao_code: '{icao_code}'
                  latitude: '{latitude}'
                  longitude: '{longitude}'                  
                  description: '{description}'                  
                  area: '{area}'                  
                  timezone_id: '{timezone_id}'                  
                  country_code_id: '{country_code_id}'                  
                  """
                  )

        db_connection.commit()

def delete_destination(destination_id):
    """
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DELETE FROM destinations WHERE destination_id = ?", (destination_id,))

        if db_cursor.rowcount == 0:
            print(f"No Destination ID found with for {destination_id}")
        else:
            print(f"Deleted Destination ID '{destination_id}'")

        db_connection.commit()
        return destination_id
