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
temp = FUNC_find_substring_return_before(".json", sys.argv[1])
NEW_filename = temp+" formatted.csv"

# making the first few mandatory lines
print("Making the first few mandatory lines...")

for string in DATA_original:
    tempTEXT = FUNC_find_substring_return_after('"m_Name": ', string, 1)
    if tempTEXT:
        DATA_new = ['Key,' + tempTEXT[1:-2] + ',NOTES,' + NEW_filename + ',\n',
                    ',,,,,,,,,,,,,,,,,,,\n',
                    'UseCyrillicFont,No,"Пометка для переводчиков: поставьте на позиции (между разделителями) вашего языка «Yes», если используете кириллицу",Yes,\n',
                    ',,,,,,,,,,,,,,,,,,,\n']
        break

# check total amount of KEYS
temp = (len(DATA_original)-20) // 9                 # first 12 strings + 8 ending strings = -20 strings; 9 strings per one key
print("KEYS total....................."+str(temp))

# making KEYS + ingame strings
print("Making KEYS + ingame strings...", end="")

string_counter = 0
key_is_opened = False
skip_next_line = False

for string in DATA_original:
    if key_is_opened:
        if skip_next_line:
            skip_next_line = False
        else:
            key_is_opened = False
            temp = string[8:-1].replace('\\"', '"')
            temp = temp.replace('\\r', '')
            temp = temp.split('\\n')

            for i in range(len(temp)):
                if temp[i] and temp[i][-1] == ' ':
                    temp[i] = temp[i][:-1]

            DATA_new[-1] += temp[0]
            for i in range(1, len(temp)):
                DATA_new[-1] += '\n'
                DATA_new.append(temp[i])
            DATA_new[-1] += ',,,\n'
    else:
        tempTEXT = FUNC_find_substring_return_after('"m_Key": ', string, 1)
        if tempTEXT:
            string_counter += 1
            print("\rMaking KEYS + ingame strings..."+str(string_counter), end="")
            DATA_new.append(tempTEXT[1:-2]+',')
            key_is_opened = True
            skip_next_line = True

# finalizing
print()
print("Writing to the file...")
FUNC_write_to_the_file(DATA_new, NEW_filename)
print()
print("------------------------------")
print("DONE! Check this file:")
print(" "+NEW_filename)
print("------------------------------")
