"""
LexCreate
Simple script to create new lexemes based on a csv list
"""
import csv
import logging
import sys

from rich import print
from consolemenu import SelectionMenu
#from simple_term_menu import TerminalMenu

from models.wikidata import WikidataLexicalCategory, Lexeme

logging.basicConfig(level=logging.DEBUG)


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
    logger = logging.getLogger(__name__)
    if len(sys.argv) > 1 < 2:
        lines = read_csv(sys.argv[1])
        if lines is not None:
            # print("List of supported lexical categories")
            # options = ["entry 1", "entry 2", "entry 3"]
            # terminal_menu = TerminalMenu(options)
            # menu_entry_index = terminal_menu.show()
            # print(f"You have selected {options[menu_entry_index]}!")
            # # List of index=QID pairs that the user can choose from
            # category_dict = {}
            # for index, category in enumerate(WikidataLexicalCategory):
            #     print(f"{index}) {category.name}")
            #     category_dict[index] = category.value
            #a_list = ["red", "blue", "green"]
            #selection = SelectionMenu.get_selection(a_list)
            menu = SelectionMenu(WikidataLexicalCategory.__members__.keys(), "Select a lexical category")
            menu.show()
            menu.join()
            selected_lexical_category_index = menu.selected_option
            category_mapping = {}
            for index, item in enumerate(WikidataLexicalCategory):
                category_mapping[index] = item
            selected_lexical_category = category_mapping[selected_lexical_category_index]
            logger.debug(f"selected:{selected_lexical_category_index}="
                         f"{selected_lexical_category}")
            exit(0)
            for line in lines:
                print(f"**Working on {line}**")
                # create Lexeme object
                lexeme = Lexeme(lemma=line, lexical_category=selected_lexical_category)
                check_if_exists(line)
                #upload
    elif len(sys.argv) > 1:
        raise Exception("cannot handle more than 1 argument")
    else:
        raise Exception("Please pass a file as argument:\n"
                        "e.g. python main.py filename.csv")