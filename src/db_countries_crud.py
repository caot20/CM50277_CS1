from src.db_handler import get_connection
from src import utils as u

def validate_input(country_code_id, alpha_2, alpha_3, country):
    """
    Validate the user input fields to make 
    sure all the values are as expected.

    Args:
        country_code_id: The Numeric Country code value (IE 826)
        alpha_2: The 2 character value of the country code (IE GB)
        alpha_3: The 2 character value of the country code (IE GBR)
        country: The country description (IE United Kingdom)
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(country_code_id, 1, 999):
        errors.append("Country Code ID must be between 1 and 999")

    if not u.validate_string(alpha_2, 2):
        errors.append("ALPHA-2 Country Code must be exactly 2 characters")

    if not u.validate_string(alpha_3, 3):
        errors.append("ALPHA-3 Country Code must be exactly 3 characters")
    
    if not u.validate_string(country, 4):
        errors.append("Country must be 4 or more characters in length")

    return errors, country_code_id, alpha_2, alpha_3, country

def validate_get_country_input(country_code_id):
    """
    Validate the user input to make 
    sure the value is as expected.

    Args:
        country_code_id: The Numeric Country code value (IE 826)
    """
    # Array to store all invalid values.
    errors = []
    if not u.validate_int(country_code_id, 0, 999):
        errors.append("Country Code ID must be between 1 and 999")

    return errors, country_code_id

def prompt_input():
    """
    Ask the user for input values so we can validate 
    and then insert/update.
    """
    print("\nEnter the Country Code ID (Leave blank to leave)")
    country_code_id = input("Country Code ID (IE 492): ")
    if not country_code_id:
        return None
    alpha_2 = input("\nEnter The 2 character value of the country code (IE MC): ").strip()
    alpha_3 = input("\nEnter The 3 character value of the country code (IE MCO): ").strip()
    country = input("\nEnter The Country description (IE Monaco): ").strip()

    errors \
    , validated_country_code_id \
    , validated_alpha_2 \
    , validated_alpha_3 \
    , validated_country = validate_input(country_code_id=country_code_id
                            , alpha_2=alpha_2
                            , alpha_3=alpha_3
                            , country=country
                            )
    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_country_code_id \
           , validated_alpha_2 \
           , validated_alpha_3 \
           , validated_country

def prompt_get_country_input():
    """
    Ask the user for input value so we can validate 
    and then return data.
    """
    print("\nEnter the Country Code ID (Leave blank to leave)")
    country_code_id = input("Country Code ID (IE 492): ")
    if not country_code_id:
        return None
    
    errors , validated_country_code_id = validate_get_country_input(country_code_id=country_code_id)

    if errors:
        print("Errors Found: ")
        for error in errors:
            print(f"- {error}")
        return None
    return validated_country_code_id 

def create_country(country_code_id, alpha_2, alpha_3, country):
    """
    Creates a new Country by Numeric value, alpha-2, alpha-3 and the Country description
    as per: https://www.iban.com/country-codes


    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("INSERT INTO countries (country_code_id, alpha_2, alpha_3, country) VALUES (?, ?, ?, ?) ON CONFLICT DO NOTHING", (country_code_id, alpha_2, alpha_3, country))
        db_connection.commit()
        return country_code_id
            
def get_countries():
    """
    Return all Countries
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT country_code_id, alpha_2, alpha_3, country FROM countries ORDER BY country_code_id ASC")
        db_connection.commit()
        return db_cursor.fetchall()

def get_country(country_code_id):
    """
    Return a single country but as an array for formatting.
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT country_code_id, alpha_2, alpha_3, country FROM countries WHERE country_code_id = ?", (country_code_id,))
        db_connection.commit()
        return db_cursor.fetchall()
    
def update_country(country_code_id, alpha_2, alpha_3, country):
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("UPDATE countries SET alpha_2 = ?, alpha_3 = ?, country = ? WHERE country_code_id = ?", (alpha_2, alpha_3, country, country_code_id))

        if db_cursor.rowcount == 0:
            print(f"No Country code id found with for {country_code_id}")
        else:
            print(f"Updated Country Code id for {country_code_id}")
        
        db_connection.commit()

def delete_country(country_code_id):
    """
    """
    with get_connection() as db_connection:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DELETE FROM Countries WHERE country_code_id = ?", (country_code_id,))

        if db_cursor.rowcount == 0:
            print(f"No Country Code ID found with for {country_code_id}")
        else:
            print(f"Deleted Country Code ID '{country_code_id}'")

        db_connection.commit()
        return country_code_id
