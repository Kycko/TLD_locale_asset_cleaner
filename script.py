from os import path as OSpath
import sys

# functions
def FUNC_exit_with_error(error_code):
    print("------------------------------")
    print(error_code)
    print("Exit...")
    sys.exit()
def FUNC_read_file(filename):
    file = open(filename, 'r')
    data = file.readlines()
    file.close()
    return data
def FUNC_find_substring(substring, string):
    index = string.find(substring)
    if index == -1:
        return 0
    else:
        return index
def FUNC_find_substring_return_after(substring, string):
    index = FUNC_find_substring(substring, string)
    if index:
        cut_from = index+len(substring)
        return string[cut_from:]
    else:
        return ""
def FUNC_find_substring_return_before(substring, string):
    index = FUNC_find_substring(substring, string)
    if index:
        return string[:index]
    else:
        return string

# MAIN PROGRAM
print("------------------------------")
print("Prepare...")
print()

if len(sys.argv) == 1:
    FUNC_exit_with_error("PLEASE ADD A FILENAME")
if not OSpath.isfile(sys.argv[1]):
    FUNC_exit_with_error("NOT FOUND: "+sys.argv[1])
DATA_original = FUNC_read_file(sys.argv[1])
temp = FUNC_find_substring_return_before(".", sys.argv[1])
NEW_filename = temp+" formatted.csv"

# making the first few mandatory lines
print("Making the first few mandatory lines...")

for string in DATA_original:
    tempTEXT = FUNC_find_substring_return_after("string m_Name = ", string)
    if tempTEXT:
        DATA_new = ['Key,' + tempTEXT[1:-1] + ',NOTES,' + NEW_filename + ',\n',
                    ',,,,,,,,,,,,,,,,,,,\n',
                    'UseCyrillicFont,No,"Пометка для переводчиков: поставьте на позиции (между разделителями) вашего языка «Yes», если используете кириллицу",Yes,\n',
                    ',,,,,,,,,,,,,,,,,,,\n']
        break
