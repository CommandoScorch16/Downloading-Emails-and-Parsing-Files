#January 11th, 2017
#Parsing emails and searching for parameters requested by the user

import tarfile
import sys
import os
import commands


outputFileName = 'emailSearchResults.txt'


#Check to see if the line of the email starts with the parameter requested for
def checkString(searchString, line):
    result = 1
    for char in range(0, len(searchString)):
        if (searchString[char] != line[char]):
            result = 0
            break
    return result


def main(argv):
    print(argv)
    if (len(argv) > 1):
        if(len(argv) > 2):
            outputFile = open(outputFileName, 'w')
            fileOfEmails = tarfile.open(argv[1], 'r')
            fileOfEmails.extractall('')
            os.chdir(fileOfEmails.getnames()[0])
            runCommand = commands.getstatusoutput
            listOfEmails = runCommand("ls")[1]
            listOfEmails = listOfEmails.split('\n')
            totalMatchesFound = 0
            for name in listOfEmails:
                email = open(name, 'r')
                foundMatch = 0
                foundList = [0]*(len(argv)-2)
                for line in email:
                    #Iterate through each of the parameters requested from the user
                    for parameter in range(2,len(argv)):
                        if (parameter == len(argv)):
                            break
                        #Convert everything to lower case so we don't miss anything!
                        if (foundList[parameter-2] == 1):
                            continue
                        if (checkString((argv[parameter].strip(':')+':').lower(), line.lower())):
                            if(foundMatch == 0):
                                outputFile.write(name + ' matches:\n')
                            foundMatch += 1
                            foundList[parameter-2] = 1
                            totalMatchesFound += 1
                            outputFile.write(line.strip('\n') + ',\n')
                outputFile.write('\n\n') 
                email.close()
            outputFile.close()
            if(totalMatchesFound > 0):
                if (totalMatchesFound > 1):
                    print('A total of %d matches were found! The result was output to %s.' % (totalMatchesFound, outputFileName))
                else:
                    print('A single match was found! The result was written to %s.' % outputFileName)
            else:
                print('No matches were found, please provide a different search criteria and try again.')
        else:
            print('No search parameters were specified. Please state what you are looking for, such as "date sent" or "subject".')
    else:
        print('No filename provided. Please provide the name of the tar file you want to parse.')


if __name__ == '__main__':
    main(sys.argv)
