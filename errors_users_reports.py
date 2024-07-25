#####!/usr/bin/env python

import csv
import re
import sys


def process_log_file(log_file_name):
    error_messages = {}   # Format {"error messaje": <count>}
    user_registers = {}   # Format {"user name": [<INFO count>, <ERROR count>]}

    #error_pattern = r"ticky: ERROR: (.+) \("
    #info_pattern  = r"ticky: INFO: (.+) \("
    pattern = r"ticky: (ERROR?|INFO?): (.+) \((\w+)\)"   # messaje type,message,username

    with open(log_file_name, "r") as file:
        lines = file.readlines()


        for line in lines:
            resp = re.search(pattern, line)

            # Check if log entry is a "ticky" messaje.
            if resp is not None:
                message_type = resp[1].strip()   # Take message type. 
                message = resp[2].strip()        # Take the message.
                username = resp[3]               # Take the username.

                # ------- Fill ERROR messages dictionary ------- #
                if "ERROR" in message_type:
                    if message in error_messages:
                        error_messages[message] += 1   # Error exist. Increment count.
                    else:
                        error_messages[message] = 1    # New error element.
                # ------- Fill ERROR messages dictionary ------- #

                # ------------ Fill USERS dictionary ----------- #
                if username not in user_registers:
                    # Create user element.abs
                    user_registers[username] = [0, 0]
                if username in user_registers:
                    if "ERROR" in message_type:
                        user_registers[username][1] += 1   # Increment user's ERROR counter
                    if "INFO" in message_type:
                        user_registers[username][0] += 1   # Increment user's INFO counter
                # ------------ Fill USERS dictionary ----------- #

        file.close()

    # Verify if any "ticky" message was processed.
    if error_messages.keys():
        # Sort ERROR dictionary from the most commun error message to the least one.
        error_messages = dict(sorted(error_messages.items(), key=lambda x : x[1], reverse=True))
        # Sort Users dictionary by username.
        user_registers = dict(sorted(user_registers.items()))

        # Create the reports.
        write_error_report(error_messages)   # Build the Error Report.
        write_user_report(user_registers)    # Build the User Report.


#
# Errors Report:
#
def write_error_report(error_messages):
    errors_report_name = "errors_report.csv"

    ### PROCEDIMIENTO "manual" de escritura de un diccionario a CSV:
    with open(errors_report_name, "w", newline="") as output_file:
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow(["Ocurrences", "Error Message"])
        for key, value in error_messages.items():
            writer.writerow([value, key])


#
# Users Report:
#
def write_user_report(user_statistics):
    users_report_name = "users_report.csv"

    ### PROCEDIMIENTO "manual":
    with open(users_report_name, "w", newline="") as output_file:
        writer = csv.writer(output_file, delimiter=',')
        writer.writerow(["User", "INFO", "ERROR"])
        for key, value in user_statistics.items():
            writer.writerow([key, value[0], value[1]])

# Este es un ejemplo de escritura de diccionario de listas.
# Tomado de: https://stackoverflow.com/questions/23613426/write-dictionary-of-lists-to-a-csv-file
# d = {"key1": [1,2,3], "key2": [4,5,6], "key3": [7,8,9]}

# keys = sorted(d.keys())

# with open("test.csv", "wb") as outfile:
#   writer = csv.writer(outfile, delimiter = "\t")
#   writer.writerow(keys)
#   writer.writerows(zip(*[d[key] for key in keys]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No syslog file to process...Please indicate log file name")
        sys.exit(1)
    else:
        log_file_name = sys.argv[1]
        log_file_name.strip()
        process_log_file(log_file_name)
        sys.exit(0)
