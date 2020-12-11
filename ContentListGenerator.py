import sys
import re
import os
from argparse import ArgumentParser

def main():
    # Register the program's command line arguments
    parser = ArgumentParser(description='Markdown contents list generator.')
    parser.add_argument("-i", "--input", dest="input", help="Specify the markdown file to generate the content list from.", type=str, required=True)
    arguments = parser.parse_args()

    # Program runtime
    print("---------------------------\nMarkdown File Content List Generator\n---------------------------")
    outputDirectoryName = "output"
    try:
        os.makedirs(outputDirectoryName)
        print(">> Creating the output directory")
    except FileExistsError:
        pass
## App entry
if __name__ == '__main__':
    main()
