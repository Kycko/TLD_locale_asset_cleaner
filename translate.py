from   os import path as OSpath
import sys

# core functions
def errorExit(msg     :str):
  print()
  print("------------------------------")
  print(msg)
  print('Exit...')
  sys.exit()
def  readFile(filename:str):
  file = open(filename,'r',encoding='utf-8')
  data = file.readlines()
  file.close()
  return data
def writeFile(data:list,filename:str):
  file = open(filename,'w',encoding='utf-8')
  file.writelines(data)
  file.close()

# string functions
def strFindSub             (sub:str,string:str):
  index = string.find(sub)
  return 0 if index == -1 else index
def strFindSub_returnAfter (sub:str,string:str,rmNewline:bool):
  index = strFindSub(sub,string)
  if index:
    cutFrom = index+len(sub)
    return string[cutFrom:len(string)-int(rmNewline)]
  else: return ''
def strFindSub_returnBefore(sub:str,string:str):
  index = strFindSub(sub,string)
  return string[:index] if index else string

# some variables
separator    = '------------------------------'
csvSeparator = ',,,,,,,,,,,,,,,,,,,\n'

# MAIN PROG
print(separator)
print('Prepare...')
if               len(sys.argv) == 1: errorExit('PLEASE ADD A FILENAME')
if not OSpath.isfile(sys.argv[1])  : errorExit('NOT FOUND: '+sys.argv[1])

dataOrig    = readFile(sys.argv[1])
temp        = strFindSub_returnBefore('.json',sys.argv[1])
newFileName = temp+' formatted.csv'

# making the first few mandatory lines
print('Making the first few mandatory lines...')

for string in dataOrig:
  tempText = strFindSub_returnAfter('"m_Name": ',string,True)
  if tempText:
    dataNew = ['Key,' + tempText[1:-2] + ',NOTES,' + newFileName + ',\n',
               csvSeparator,
               'UseCyrillicFont,No,"Пометка для переводчиков: поставьте на позиции (между разделителями) вашего языка «Yes», если используете кириллицу",Yes,\n',
               csvSeparator]
    break

# check total amount of KEYS
temp = (len(dataOrig)-20) // 9  # first 12 strings + 8 ending strings = -20 strings; 9 strings per one key
print('KEYS total.....................'+str(temp))

# making KEYS + ingame strings
print('Making KEYS + ingame strings...', end='')

strCounter             = 0
keyOpened,skipNextLine = False,False

for string in dataOrig:
  if keyOpened:
    if skipNextLine: skipNextLine = False
    else:
      keyOpened = False
      temp      = string[8:-1].replace('\\"','"')
      temp      = temp        .replace('\\r','')
      temp      = temp          .split('\\n')

      for i in range(len(temp)):
        if temp[i] and temp[i][-1] == ' ': temp[i] = temp[i][:-1]

      dataNew[-1] += temp[0]
      for i in range(1,len(temp)):
        dataNew[-1] += '\n'
        dataNew.append(temp[i])
      dataNew[-1] += ',,,\n'
  else:
    tempText = strFindSub_returnAfter('"m_Key": ',string,True)
    if tempText:
      strCounter += 1
      print('\rMaking KEYS + ingame strings...'+str(strCounter),end='')
      dataNew.append(tempText[1:-2]+',')
      keyOpened,skipNextLine = True,True

# finalizing
print    ()
print    ('Writing to the file...')
writeFile( dataNew,newFileName)
print    ()
print    (separator)
print    ('DONE! Check this file:')
print    (' '+newFileName)
print    (separator)
