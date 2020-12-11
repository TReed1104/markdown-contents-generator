import sys
import re
import os
from argparse import ArgumentParser

## Extract the titles from the markdown
def parseMarkdownFile(filePath):
    return
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

    ## Check we have an input file
    if arguments.input is not None:
        parseMarkdownFile(arguments.input)

## App entry
if __name__ == '__main__':
    main()
