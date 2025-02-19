
import os
import sys
import markdown as md

def filecheck_md():
  # check if md file exists
  if os.path.exists("GithubReadme.md"):
    os.remove("GithubReadme.md")
  else:
    print("The file does not exist")

def filecheck_txt():
  # check if md file exists
  if os.path.exists("GithubReadme.txt"):
    os.remove("GithubReadme.txt")
  else:
    print("The file does not exist")