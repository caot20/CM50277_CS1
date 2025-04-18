from src import db_timezones_crud as tz
from src import menus as m

def timezones_menu_options():
    """
    """
    return {
        "1": ("Display Timezones", display_timezones),
        "2": ("Display Timezone", display_timezone),
        "3": ("Create Timezone", create_timezone),
        "4": ("Update Timezone", update_timezone),
        "5": ("Delete Timezone", delete_timezone),
        "0": ("Back", m.main_menu)
    }

def display_timezones():
    """
    Display all the Timezones.
    """
    rows = tz.get_timezones()
    if rows:
        print_timezones(rows=rows)
    else:
        print("Query returned no results.")

def display_timezone():
    """
    Display a single timezone.
    """
    while True:
        data = tz.prompt_get_timezone_input()
        if data is None:
            print("Exiting Display Timezone...")
            break

        validated_timezone_id = data

        rows = tz.get_timezone(timezone_id=validated_timezone_id)
        if rows:
            print_timezones(rows=rows)
        else:
            print("Query returned no results.")

        see_more = input("\nDisplay another Timezone? (y/n): ").strip().lower()
        if see_more != 'y':
            print("Exiting Display Timezone...")
            break

def print_timezones(rows):
    """
    Print out results to console in a Table Like Output with Fixed Width
    """
    print(f"| {'Timezone ID':<12} | {'Timezone':<20} | {'UTC Offset':<10} |")
    print('-' * 52)
    for row in rows:
        print(f"| {row[0]:<12} | {row[1]:<20} | {row[2]:<10} |")

def create_timezone():
    """
    Validate and Create a Timezone
    """
    while True:
        data = tz.prompt_insert_input()
        if data is None:
            print("Exiting Create Timezone...")
            break

        validated_timezone \
           , validated_utc_offset = data

        timezone_id = tz.create_timezone(validated_timezone
                                         , validated_utc_offset
                                        )
        if timezone_id > 0:
            print(f"Added timezone '{validated_timezone}' with offset '{validated_utc_offset}' and new timezone_id created as '{timezone_id}'")
        else:
            print(f"Timezone '{validated_timezone}' with offset '{validated_utc_offset}' not created")

        add_more = input("\nAdd another Timezone? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Create Timezone...")
            break

def update_timezone():
    """
    Validate and Update a Timezone
    """
    while True:
        data = tz.prompt_update_input()
        if data is None:
            print("Exiting Update Country...")
            break

        validated_timezone_id \
           , validated_timezone \
           , validated_utc_offset = data

        tz.update_timezone(timezone_id=validated_timezone_id
                         , timezone=validated_timezone
                         , utc_offset=validated_utc_offset
                         )
        add_more = input("\nUpdate another Timezone? (y/n): ").strip().lower()
        if add_more != 'y':
            print("Exiting Update Timezone...")
            break

def delete_timezone():
    """
    Validate and Delete a Timezone
    """
    while True:
        data = tz.prompt_get_timezone_input()
        if data is None:
            print("Exiting Delete Timezone...")
            break

        validated_timezone_id = data

        tz.delete_timezone(timezone_id=validated_timezone_id)

        delete_more = input("\nDelete another Timezone? (y/n): ").strip().lower()
        if delete_more != 'y':
            print("Exiting Delete Timezone...")
            break
