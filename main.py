# Pip dependancies
from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time
import markdown as md
from prettytable import PrettyTable
from prettytable import TableStyle
import os
import sys
import numpy as np
# My imports
import fileUlti as fu


console = Console()

# Using Inquirepy to create some questions to ask the user
questions = [
    {"type" : "input" , "name" : "title" , "message" : "Project Title"},
    {"type" : "input" , "name" : "description" , "message" : "Project Description"},
    {"type" : "input" , "name" : "installation" , "message" : "Installation Instructions"},
    {"type" : "input" , "name" : "usage" , "message" : "Usage Instructions"},
    {
        "type" : "list",
        "name" : "license",
        "message" : "Choose a License",
        "choices" : [
            "MIT License",
            "Apache License 2.0",
            "GNU GPLv3",
            "GUN LGPLv3",
            "Mozilla Public License 2.0",
            "Creative Commons",
            "The Unlicense"
        ],
    },
    {"type" : "input" , "name" : "author", "message" : "Author / Contact Info"}

]
answers = prompt(questions)
# print(answers)

# Take some elements out of user 's answers array store them into variables.
title = answers["title"]
description = answers["description"]
installation = answers["installation"]
usage = answers["usage"]
license = answers["license"]
author = answers["author"]

# take the dictionaries keys, values and assign them to some variables
Entry_dict = { "## Project Title: ": title, "## Project Description: ": description, "## Installation Instructions: ": installation, "## Usage Instructions: ": usage, "## Chose a License": license, "## Author / Contact Info: ": author}
x = str(Entry_dict.keys())
y = str(Entry_dict.values())

# Show a progress bar
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

console.print("[bold green]Task Complete![/bold green] ✅")

# Random Matrix table
matrix = np.random.randint(10, size=(3, 3))
table = PrettyTable()
table.set_style(TableStyle.MARKDOWN)
for i in range (3):
    table.add_row([matrix[i]])
table.header = False
# print(table)

# check if files exists
fu.filecheck_md()
fu.filecheck_txt()

# write the output to a markdown file

with open('readme.md', 'ab+') as f:

    for key, value in Entry_dict.items():
        f.write(f'{key}\n'.encode())
        f.write(f'{value}\n'.encode())
    
    f.write('## Random Matrix \n'.encode())
    f.write(f'{table}\n'.encode())
    

print("Markdown File created successfully. Well done check out this cool random matrix table below")


md.markdownFromFile(input=open("readme.md", "rb"), output=open("out.html", "wb"))

# write the output to a txt file
with open('readme.txt', 'w') as w:
    # w.write(table.get_string())

    for key, value in Entry_dict.items():
        w.write(f'{key}\n')
        w.write(f'{value}\n')
    w.write(f'{table}\n')
print("Txt file created successfully")
        
