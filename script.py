from os import path as OSpath
import sys

# functions
def exit_with_error(error_code):
    print("------------------------------")
    print(error_code)
    print("Exit...")
    sys.exit()

# main program
print("------------------------------")
print("Prepare...")
print()

if len(sys.argv) == 1:
    exit_with_error("PLEASE ADD A FILENAME")
if not OSpath.isfile(sys.argv[1]):
    exit_with_error("NOT FOUND: "+sys.argv[1])
