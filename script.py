from os import path as OSpath
import sys

# functions
def FUNC_exit_with_error(error_code):
    print()
    print("------------------------------")
    print(error_code)
    print("Exit...")
    sys.exit()
def FUNC_read_file(filename):
    file = open(filename, 'r', encoding='utf-8')
    data = file.readlines()
    file.close()
    return data
def FUNC_write_to_the_file(data, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.writelines(data)
    file.close()
def FUNC_find_substring(substring, string):
    index = string.find(substring)
    if index == -1:
        return 0
    else:
        return index
def FUNC_find_substring_return_after(substring, string, remove_newline):                # string, string, int(0/1)
    index = FUNC_find_substring(substring, string)
    if index:
        cut_from = index+len(substring)
        return string[cut_from:len(string)-1*remove_newline]
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

if len(sys.argv) == 1:
    FUNC_exit_with_error("PLEASE ADD A FILENAME")
if not OSpath.isfile(sys.argv[1]):
    FUNC_exit_with_error("NOT FOUND: "+sys.argv[1])
DATA_original = FUNC_read_file(sys.argv[1])
temp = FUNC_find_substring_return_before(".txt", sys.argv[1])
NEW_filename = temp+" formatted.csv"

# making the first few mandatory lines
print("Making the first few mandatory lines...")

for string in DATA_original:
    tempTEXT = FUNC_find_substring_return_after("string m_Name = ", string, 1)
    if tempTEXT:
        DATA_new = ['Key,' + tempTEXT[1:-1] + ',NOTES,' + NEW_filename + ',\n',
                    ',,,,,,,,,,,,,,,,,,,\n',
                    'UseCyrillicFont,No,"Пометка для переводчиков: поставьте на позиции (между разделителями) вашего языка «Yes», если используете кириллицу",Yes,\n',
                    ',,,,,,,,,,,,,,,,,,,\n']
        break

# check total amount of KEYS
temp_counter = False
for string in DATA_original:
    tempTEXT = FUNC_find_substring_return_after("int size = ", string, 1)
    if tempTEXT:
        if temp_counter:
            print("KEYS total....................."+tempTEXT)
            break
        else:
            temp_counter = True

# finalizing
FUNC_write_to_the_file(DATA_new, NEW_filename)
print("\n------------------------------")
print("DONE!")
print("------------------------------")
