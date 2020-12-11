import re
import os
from datetime import datetime
from argparse import ArgumentParser

## Write the contents list to text file
def writeContentListToFile(contentListDict):
    print(">> Writing Output File...")
    try:
        fileTitle = "output/content_list_" + datetime.now().strftime("%Y%d%m_%H%M%S") + ".md"   ## Generate the file name
        outputFile = open("fileTitle", "w")   ## Open the file to output to
        ## Iterate our chapter titles
        for mainTitleKey in contentListDict:
            outputFile.write(mainTitleKey + "\n")
            ## Iterate the chapter sub-titles
            for subTitleKey in contentListDict[mainTitleKey]:
                outputFile.write("\t" + subTitleKey + "\n")
        outputFile.close()                          ## Close the file and save the output
        print(">> Output Saved!")
    except (OSError, IOError) as e:
        ## Catch errors in the file stream
        print(">>>> ERROR! - An error occured: ", e)

## Parse the title list into a content list
def generateContentsList(markDownTitleList):
    print(">> Parsing Titles...")
    generatedContentsList = {}
    chapterCount = 0
    lastTitle = ""
    ## Iterate through each title and generate its entry in the contents list
    for title in markDownTitleList:
        ## Check if the title is a chapter title
        if title.count('#') == 2:
            chapterCount += 1
            titleName = title.replace('##', '').strip()
            titleNameTag = re.sub(r'([^\s\w]|_)+', '', titleName).lower().replace(' ', '-')
            contentListEntry = str(chapterCount) + ". [" + titleName + "](" + titleNameTag + ")"
            lastTitle = contentListEntry
            generatedContentsList[contentListEntry] = {}
        ## Check if the title is a sub-title
        elif title.count('#') == 3:
            titleName = title.replace('###', '').strip()
            titleNameTag = re.sub(r'([^\s\w]|_)+', '', titleName).lower().replace(' ', '-')
            contentListEntry = "* [" + titleName + "](" + titleNameTag + ")"
            generatedContentsList[lastTitle][contentListEntry] = {}
    ## Write the content list to file
    writeContentListToFile(generatedContentsList)

## Extract the titles from the markdown
def parseMarkdownFile(filePath):
    print(">> Reading file...")
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
