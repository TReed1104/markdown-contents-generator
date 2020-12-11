import sys
import re
import os
from argparse import ArgumentParser

## Parse the title list into a content list
def generateContentsList(markDownTitleList):
    print(markDownTitleList)
    return

## Extract the titles from the markdown
def parseMarkdownFile(filePath):
    markdownTitleList = []              ## List of all the found titles in the markdown file
    markdownFile = open(filePath, "r")  ## Open the markdown file
    ## Read the file
    for line in markdownFile:
        ## If the line starts with a title marker
        if line[0:6].find("#") != -1:
            line = line.replace('\r', '').replace('\n', '') ## Strip the carriage returns and newlines
            line.strip()    ## Strip and pre/post whitespace
            markdownTitleList.append(line)
    markdownFile.close()                ## Close the markdown file

    ## Pass the title list to the content list generator
    generateContentsList(markdownTitleList)

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
