
import argparse
import json
import sys

def main(fileToRead):
    fileNameList = getFileNameList(fileToRead)
    countList = countExtensions(fileNameList)
    printResults(countList)

def getFileNameList(fileToRead):
    fileNameList = set()

    #Parse all valid json and add the nm field to a set.
    #Use set because entries in a set have to be unique, so there will be no duplicate filenames.
    with open(fileToRead) as fileReader:
        for line in fileReader:
            try:
                parsedLine = json.loads(line)
            except:
                pass

            fileNameList.add(parsedLine.get('nm'))

    return fileNameList

def countExtensions(fileNameList):
    #Count the extensions using a dictionary
    extensionCountList = {}

    for fileName in fileNameList:
        extension = fileName.rpartition(".")[2]
        if (extensionCountList.get(extension)):
            extensionCountList[extension] += 1
        else:
            extensionCountList[extension] = 1

    return  extensionCountList

def printResults(countList):
    [print(k + ':' + str(v)) for k, v in countList.items()]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='File extension counter program')
    parser.add_argument("file", type=str, help='Json file to parse.')
    args = parser.parse_args()

    main(args.file)

