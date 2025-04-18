import os
from datetime import datetime
import re


def validate_string(string_param, string_length):
    """
    """
    if string_param is None: 
        raise ValueError("Parameter cannot be None")
    if not isinstance(string_param, str):
        raise ValueError(f"Parameter must be a string, got {type(string_param).__name__}")
    if len(string_param) < string_length:
        raise ValueError(f"Parameter string length must be greater than or equal to {string_length}")
    return True

def validate_int(int_param, min, max):
    """
    """
    if int_param is None: 
        raise ValueError("Parameter cannot be None")
    if isinstance(int_param, int):
        return True
    if int(int_param) <= min and int(int_param) >= max:
        raise ValueError(f"Parameter must be between {min} and {max}")
    return True

def validate_offset(int_param):
    """
    """
    if int_param is None: 
        raise ValueError("Parameter cannot be None")
    if isinstance(int_param, float):
        return True
    if float(int_param) <= -12.0 and float(int_param) > 14.0:
        raise ValueError("Parameter must be between -12.0 and 14.0")
    return True

def validate_real(int_param):
    """
    """
    if int_param is None: 
        raise ValueError("Parameter cannot be None")
    if isinstance(int_param, float):
        return True
    return True

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_iso8601(string_date):
    """
    Validates if a string is in the ISO 8601 Format
    """
    if string_date is None: 
        raise ValueError("Parameter cannot be None")
    
    try:
        # Basic regex to check ISO 8601 pattern
        iso8601_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{1,6})?([+-]\d{2}:\d{2}|Z)?$'
        if not re.match(iso8601_pattern, string_date):
            return False
        
        # Parse the string to ensure it's a valid date
        datetime.fromisoformat(string_date.replace('Z', '+00:00'))
        return True
    except ValueError:
        return False
