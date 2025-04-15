#  This script will automate the analysis of server logs,
#  specifically looking for error messages and counting occurrences of each unique error.


import re
from collections import Counter

log_file_path = '/var/log/syslog'  # Change this to an appropriate file pat


error_pattern = r'ERROR|FAIL|CRITICAL|SEVERE'


def analyze_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()

    error_messages = re.findall(error_pattern, log_data)    # Find all occurrences of error messages using the regex pattern

    error_count = Counter(error_messages)

    return error_count



if __name__ == '__main__':
    print(f"Analyzing log file: {log_file_path}")
    errors = analyze_log(log_file_path)

    # Output the result
    if errors:
        print("Error summary:")
        for error, count in errors.items():
            print(f"{error}: {count} occurrences")
    else:
        print("No errors found.")
