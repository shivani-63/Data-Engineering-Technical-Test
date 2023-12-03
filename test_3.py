"""Adapted function to sum a given time as a string."""
### TESTS CAN BE FOUND IN THE test_test_3.py FILE ###

def sum_current_time(time_str: str) -> int:
    """Expects data in the format HH:MM:SS"""
    # guard clause to ensure the input is a string (therefore can be split in the next step).
    if not isinstance(time_str,str):
        raise TypeError("Input must be a string")

    # splitting the string to a list of integers and converting the strings to integers.
    try:
        list_of_nums_str = time_str.split(":")
        list_of_nums_int = [int(num) for num in list_of_nums_str]
    except:
        raise ValueError("Input must be in the HH:MM:SS format.")

    # asserting integers are valid numbers for a timestamp
    if list_of_nums_int[0] > 23:
        raise ValueError("Input must have a valid hour between 0-23.")
    if list_of_nums_int[1] > 59 or list_of_nums_int[2] > 59:
        raise ValueError("Input must have valid minutes/seconds between 0-59.")

    return sum(list_of_nums_int)


if __name__ == "__main__":

    print(sum_current_time('01:02:03'))
