#January 11th, 2017
#Parsing emails and searching for parameters requested by the user

import tarfile
import sys
import os
import commands

#Check to see if the line of the email starts with the parameter requested for
def checkString(searchString, line):
    result = 1
    for char in range(0, len(searchString)):
        if (searchString[char] != line[char]):
            result = 0
            break
    return result


def main(argv):
    if (len(argv) > 1):
        if(len(argv) > 2):
            outputFile = open('emailSearchResults.txt', 'w')
            fileOfEmails = tarfile.open(argv[1], 'r')
            fileOfEmails.extractall('')
            os.chdir(fileOfEmails.getnames()[0])
            runCommand = commands.getstatusoutput
            listOfEmails = runCommand("ls")[1]
            listOfEmails = listOfEmails.split('\n')
            for name in listOfEmails:
                email = open(name, 'r')
                foundMatch = 0
                for line in email:
                    #Iterate through each of the parameters requested fro
                    for parameter in argv[2:]:
                        #Convert everything to lower case so we don't miss anything!
                        if (checkString((parameter.strip(':')+':').lower(), line.lower())):
                            if(foundMatch == 0):
                                outputFile.write(name + ' matches:\n')
                                foundMatch = 1
                            outputFile.write(line.strip('\n') + ',\n')
                outputFile.write('\n\n') 
                email.close()
            outputFile.close()
            return 1
        else:
            print('No search parameters were specified. Please state what you are looking for, such as "date sent" or "subject".')
    else:
        print('No filename provided. Please provide the name of the tar file you want to parse.')

if __name__ == '__main__':
    main(sys.argv)
