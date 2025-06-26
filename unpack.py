from   os  import path as OSpath
from   sys import argv
from   sys import exit as sysExit
import json
import UnityPy

# ↓ change if you need other languages
langs = ('English','Russian') # should match asset names in the localization file

def errorExit(msg:str):
  print()
  print('------------------------------')
  print(msg)
  print('Exit...')
  sysExit()

if len(argv) == 1: errorExit('PLEASE ADD A FILENAME')
file = argv[1]
if not OSpath.isfile(file): errorExit('NOT FOUND: '+file)

for  obj in UnityPy.load(file).objects:
  if obj.type.name == 'MonoBehaviour' and obj.serialized_type.node:
    tree = obj.read_typetree()
    lang = tree['m_Name']
    if lang in langs:
      fName = lang+'.json'
      with   open( fName,'wt',encoding    ='utf8') as f:
        json.dump( tree,  f  ,ensure_ascii= False,indent=4)
        print    ('Export done → '+fName)
