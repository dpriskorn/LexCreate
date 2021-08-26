"""
LexCreate
Simple script to create new lexemes based on a csv list
"""
import csv
import sys

from rich import print
#from simple_term_menu import TerminalMenu

from models.wikidata import WikidataLexicalCategory


def read_csv(filepath):
    lines = []
    with open(filepath, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        for line in csvFile:
            # Strip the first column
            lines.append(line[0].strip())
    return lines


def check_if_exists(line):
    print("check if exist")
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1 < 2:
        lines = read_csv(sys.argv[1])
        if lines is not None:
            print("List of supported lexical categories")
            # Import the necessary packages
            from consolemenu import *
            from consolemenu.items import *

            # Create the menu
            menu = ConsoleMenu("Title", "Subtitle")

            # Create some items

            # MenuItem is the base class for all items, it doesn't do anything when selected
            menu_item = MenuItem("Menu Item")

            # A FunctionItem runs a Python function when selected
            function_item = FunctionItem("Call a Python function", input, ["Enter an input"])

            # A CommandItem runs a console command
            command_item = CommandItem("Run a console command", "touch hello.txt")

            # A SelectionMenu constructs a menu from a list of strings
            selection_menu = SelectionMenu(["item1", "item2", "item3"])

            # A SubmenuItem lets you add a menu (the selection_menu above, for example)
            # as a submenu of another menu
            submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

            # Once we're done creating them, we just add the items to the menu
            menu.append_item(menu_item)
            menu.append_item(function_item)
            menu.append_item(command_item)
            menu.append_item(submenu_item)

            # Finally, we call show to show the menu and allow the user to interact
            menu.show()
            # options = ["entry 1", "entry 2", "entry 3"]
            # terminal_menu = TerminalMenu(options)
            # menu_entry_index = terminal_menu.show()
            # print(f"You have selected {options[menu_entry_index]}!")
            # # List of index=QID pairs that the user can choose from
            # category_dict = {}
            # for index, category in enumerate(WikidataLexicalCategory):
            #     print(f"{index}) {category.name}")
            #     category_dict[index] = category.value
            exit(0)
            lexical_category = input("What lexical category?")
            for line in lines:
                print(f"**Working on {line}**")
                # create Lexeme object
                lexeme = Lexeme(lemma=line, lexical_category=options[menu_entry_index])
                check_if_exists(line)
                #upload
    elif len(sys.argv) > 1:
        raise Exception("cannot handle more than 1 argument")