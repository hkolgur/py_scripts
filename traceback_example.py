"""usage of trace back to extract, format and print stack traces"""

import traceback


def cause_error():
    """divide number by zero"""
    return 1 / 0


try:
    cause_error()
except ZeroDivisionError:
    # 1. Print the traceback directly to the console
    # Useful for immediate debugging
    print("---------------------print_exc Begin--------------------------------")
    traceback.print_exc()
    print("---------------------print_exc End--------------------------------")

    # 2. Get the traceback as a string
    # Useful for logging to a file or sending to an error monitoring service
    error_string = traceback.format_exc()
    print("---------------------format_exc Begin--------------------------------")
    print(f"\n--- Captured Traceback String ---\n{error_string}")
    print("---------------------format_exc End--------------------------------")
