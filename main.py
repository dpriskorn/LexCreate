"""
LexCreate
Simple script to create new lexemes based on a csv list
"""
import csv
import logging
import sys
from pprint import pprint
from typing import List

from rich import print
from consolemenu import SelectionMenu
#from simple_term_menu import TerminalMenu

from models.wikidata import WikidataLexicalCategory, Lexeme, WikimediaLanguageCode

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


def select_lexical_category():
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
    return selected_lexical_category


def select_language():
    menu = SelectionMenu(WikimediaLanguageCode.__members__.keys(), "Select a language")
    menu.show()
    menu.join()
    selected_language_index = menu.selected_option
    mapping = {}
    for index, item in enumerate(WikimediaLanguageCode):
        mapping[index] = item
    selected_language = mapping[selected_language_index]
    logger.debug(f"selected:{selected_language_index}="
                 f"{selected_language}")
    return selected_language


def ask_if_duplicate(json: List) -> bool:
    print(f"Found: **{json['label']}** {json['description']}, see {json['uri']}")
    answer = input(f"Is this a duplicate? [Y/n]")
    if answer == "" or answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
    else:
        # TODO make a while loop and restart instead of failing
        raise Exception(f"Could not understand {answer}")


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    if len(sys.argv) > 1 < 2:
        lines = read_csv(sys.argv[1])
        if lines is not None:
            # TODO enable setting language and lexical category via the command line
            selected_language = select_language()
            selected_lexical_category = select_lexical_category()
            for line in lines:
                print(f"**Working on {line}**")
                # create Lexeme object
                lexeme = Lexeme(lemma=line, lexical_category=selected_lexical_category,
                                language_code=selected_language)
                duplicates = lexeme.find_duplicates()
                if duplicates is not None:
                    print("Duplicate(s) found")
                    # pprint(duplicates)
                    for duplicate in duplicates:
                        answer = ask_if_duplicate(duplicate)
                        if answer:
                            logger.debug("Marked as duplicate, skipping")
                            continue
                        else:
                            print(f"{lexeme.lemma} ready for upload")
                    exit(0)
                else:
                    logger.debug("No duplicate found")
                    print(f"{lexeme.lemma} ready for upload")
                #upload
    elif len(sys.argv) > 1:
        raise Exception("cannot handle more than 1 argument")
    else:
        raise Exception("Please pass a file as argument:\n"
                        "e.g. python main.py filename.csv")