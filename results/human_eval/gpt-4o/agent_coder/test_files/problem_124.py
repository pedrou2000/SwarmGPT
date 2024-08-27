
def valid_date(date):
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    for example: 
    valid_date('03-11-2000') => True

    valid_date('15-01-2012') => False

    valid_date('04-0-2040') => False

    valid_date('06-04-2020') => True

    valid_date('06/04/2020') => False
    """


import re

def valid_date(date: str) -> bool:
    """Check if the given date string is valid according to the specified rules."""
    
    # Rule 1: The date string is not empty
    if not date:
        return False
    
    # Rule 4: The date should be in the format: mm-dd-yyyy
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    
    # Extract month, day, and year
    month, day, year = map(int, date.split('-'))
    
    # Rule 3: The months should not be less than 1 or higher than 12
    if month < 1 or month > 12:
        return False
    
    # Rule 2: Validate the day based on the month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 1 <= day <= 31
    elif month in {4, 6, 9, 11}:
        return 1 <= day <= 30
    elif month == 2:
        return 1 <= day <= 29
    
    # If none of the conditions are met, return False
    return False

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False

def check(candidate):

    # Check some simple cases
    assert candidate('03-11-2000') == True

    assert candidate('15-01-2012') == False

    assert candidate('04-0-2040') == False

    assert candidate('06-04-2020') == True

    assert candidate('01-01-2007') == True

    assert candidate('03-32-2011') == False

    assert candidate('') == False

    assert candidate('04-31-3000') == False

    assert candidate('06-06-2005') == True

    assert candidate('21-31-2000') == False

    assert candidate('04-12-2003') == True

    assert candidate('04122003') == False

    assert candidate('20030412') == False

    assert candidate('2003-04') == False

    assert candidate('2003-04-12') == False

    assert candidate('04-2003') == False

check(valid_date)