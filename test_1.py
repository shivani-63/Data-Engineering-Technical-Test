"""Script to validate log lines and then convert each log string to a dictionary object."""

def is_log_line(line):
    """Takes a log line and returns True if it is a valid log line and returns nothing
    if it is not.
    """
    valid_error_types = ["WARNING", "INFO", "TRACE"]
    for error_type in valid_error_types:
        #this ensures an error type and the ':' syntax for the start of each message is in the log line.
        if error_type in line and ":" in line:
            return True
    return False

def get_dict(line):
    """Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
    #getting the timestamp from the line string
    timestamp = line[:17]

    #splitting the string into a list to get the log_level as a separate entity
    line_to_get_log_level = line.split(" ")
    log_level = line_to_get_log_level[2]

    #splitting the string again, by two spaces to isolate the message this time
    line_to_get_message = line.split("  ")
    #getting the message as the second thing in the list, and cutting off the new line syntax
    message = line_to_get_message[2][:-1]

    return {"timestamp": timestamp, "log_level": log_level, "message": message}



if __name__ == "__main__":
    # these are basic generators that will return
    # 1 line of the log file at a time
    def log_parser_step_1(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

    def log_parser_step_2(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield get_dict(line)

    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE

    def test_step_1():
        with open("tests/step1.log") as f:
            test_lines = f.readlines()
        actual_out = list(log_parser_step_1("sample.log"))

        if actual_out == test_lines:
            print("STEP 1 SUCCESS")
        else:
            print(
                "STEP 1 FAILURE: step 1 produced unexpecting lines.\n"
                "Writing to failure.log if you want to compare it to tests/step1.log"
            )
            with open("step-1-failure-output.log", "w") as f:
                f.writelines(actual_out)

    def test_step_2():
        expected = {
            "timestamp": "03/11/21 08:51:01",
            "log_level": "INFO",
            "message": ":.main: *************** RSVP Agent started ***************",
        }
        actual = next(log_parser_step_2("sample.log"))

        if expected == actual:
            print("STEP 2 SUCCESS")
        else:
            print(
                "STEP 2 FAILURE: your first item from the generator was not as expected.\n"
                "Printing both expected and your output:\n"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {actual}")

    try:
        test_step_1()
    except Exception:
        print("step 1 test unable to run")

    try:
        test_step_2()
    except Exception:
        print("step 2 test unable to run")
