
import os
import sys
import markdown as md

def filecheck_md():
  # check if md file exists
  if os.path.exists("readme.md"):
    os.remove("readme.md")
  else:
    print("The file does not exist")

def filecheck_txt():
  # check if md file exists
  if os.path.exists("readme.txt"):
    os.remove("readme.txt")
  else:
    print("The file does not exist")