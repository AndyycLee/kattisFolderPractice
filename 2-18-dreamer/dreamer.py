"""
how does backtracking make choices from the pool of choices? if it can skip certain choices? since in something like n queens, the choice is to first look at all cases startong from a queen at 0..8

whereas this has a choice at index 0..8, but the choice if at 1, we need to reuse digit at 0

but actually, these are identical patterns, right

in both backtracking appraoches with kattis dreamer and n queens. we try to make a choice out of every possible choice. we just continue if the choice that wed make is invalid (for n queens, it occupies the col or diagonal), 
(for dreamer, that means digits we have already used, or rather the index of the digit we have used)

In both cases, your "pool" is a fixed set of options. The only difference is what makes an option "invalid."

In N-Queens: The pool is columns 0 to N-1. You can't pick column 3 if a queen is already there or if it's diagonal to another.

In Dreamer: The pool is digit-indices 0 to 7. You can't pick index 3 if you already used it for a previous position in your current date string
"""

valid_dates = set()

used = set()
path = ["", "", "", "", "", "", "", ""]

def is_valid_date(day, month, year):
    if year < 2000:
        return False
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    if day > days_in_month[month - 1]:
        return False
    return True

def helper(i, digits):
# Base case: we've placed all 8 digits
    if i == 8:
        # Validate the date formed by path
        day = int("".join(path[0:2]))
        month = int("".join(path[2:4]))
        year = int("".join(path[4:8]))
        if is_valid_date(day, month, year):
            valid_dates.add("".join(path))
        return

    # choices
    for idx, digit in enumerate(digits):
        if idx in used:  # Skip if this digit already used
            continue
        if i == 1:
            potential_day = int(path[0] + digit)
            if potential_day > 31 or potential_day == 0:
                continue
        
        if i == 3:  # About to complete the month
            potential_month = int(path[2] + digit)
            if potential_month > 12 or potential_month == 0:
                continue
        if i == 7:  # About to complete the year
            potential_year = int("".join(path[4:7]) + digit)
            if potential_year < 2000:
                continue
        path[i] = digit
        used.add(idx) 
        helper(i+1, digits)
        used.remove(idx)
        path[i] = ""

def customSortKey(date):
    day, month, year = int(date[0:2]), int(date[2:4]), int(date[4:])
    return (year, month, day)

test_cases = int(input())
# date format is ddmmyyyy
for _ in range(test_cases):
    date_input = input()

    digits = "".join(date_input.split())
    
    helper(0, digits)
    l = len(valid_dates)

    if l != 0:
        sorted_dates = sorted(valid_dates, key=customSortKey)
        earliestDate = sorted_dates[0]
        day, month, year = earliestDate[0:2], earliestDate[2:4], earliestDate[4:]
        
        print(f"{l} {day} {month} {year}")
    else:
        print(0)

#   CLEAR the globals for the next test case
    valid_dates.clear()
    used.clear()