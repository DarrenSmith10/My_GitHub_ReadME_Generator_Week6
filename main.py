from InquirerPy import prompt
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
import time
import markdown as md
import numGenerator as ng
import os
import sys
from prettytable import PrettyTable
from prettytable import TableStyle



console = Console()
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

# take the dictionaries key and assign it to a variable
title = answers["title"]
description = answers["description"]
installation = answers["installation"]
usage = answers["usage"]
license = answers["license"]
author = answers["author"]


Entry_dict = { "## Project Title: ": title, "## Project Description: ": description, "## Installation Instructions: ": installation, "## Usage Instructions: ": usage, "## Chose a License": license, "## Author / Contact Info: ": author}
# x = Entry_dict.keys()
# y = Entry_dict.values()
# print(x)
# print(y)
# print the variables test

# Show a progress bar
with Progress() as progress:
    task = progress.add_task("Processing...", total=100)
    for _ in range(10):
        time.sleep(0.3)
        progress.update(task, advance=10)

console.print("[bold green]Task Complete![/bold green] ✅")

# Create a table using Rich
# table = Table(title="GitHub Readme Generator")

# table.add_column("Info", justify="center", style="cyan", no_wrap=True)
# table.add_column("Result", justify="centre", style="magenta")

# for key,values in Entry_dict.items():
#     table.add_row(key, values)

# console.print(table)

table = PrettyTable()
table.set_style(TableStyle.MARKDOWN)
table.field_names = ["Info","Result"]
for key, value in Entry_dict.items():
     table.add_row([key, value])

print(table)

# check if md file exists
if os.path.exists("readmetest3.md"):
  os.remove("readmetest3.md")
else:
  print("The file does not exist")

# now assign the variables to a markdown file

with open('readmetest3.md', 'ab+') as f:

    # for key, value in Entry_dict.items():
    #     f.write(f'{key}\n'.encode())
    #     f.write(f'{value}\n'.encode())
    f.write(f'{table}\n'.encode())
    # f.write('## Matrix Table\n'.encode())
    # f.write('```table\n'.encode())


md.markdownFromFile(input=open("readmetest3.md", "rb"), output=open("out.html", "wb"))


original_stdout = sys.stdout

# Redirect stdout to a file
with open('output.txt', 'w') as w:
    w.write(table.get_string())
