import unittest
import commands
import os
class ParseEmailTestMethods(unittest.TestCase):

    #Check to see if the line of the email starts with the parameter requested for, just like in parseEmails.py
    def checkString(self, searchString, line):
        result = 1
        for char in range(0, len(searchString)):
            if (searchString[char] != line[char]):
                result = 0
                break
        return result


    def parseMessages(self, searchParameter):
        outputFile = open('emailSearchResults.txt', 'r')
        timesFound = 0
        for line in outputFile:
            result = self.checkString(searchParameter.lower(), line.lower())
            if (result == 1):
                timesFound += 1
        return timesFound

    def testSubject(self):
        runCommand = commands.getstatusoutput
        output = runCommand('sudo python parseEmails.py sampleEmails.tar.gz "Subject"') 
        self.assertEquals('A total of 12 matches were found! The result was output to emailSearchResults.txt.', (output[1].split('\n'))[1] )
        timesFound = self.parseMessages('Subject')
        self.assertEquals(timesFound, 12)

    def testDate(self):
        runCommand = commands.getstatusoutput
        output = runCommand('sudo python parseEmails.py sampleEmails.tar.gz "Date"')
        self.assertEquals('A total of 12 matches were found! The result was output to emailSearchResults.txt.', (output[1].split('\n'))[1] )
        timesFound = self.parseMessages('Date')
        self.assertEquals(timesFound, 12)

    def testFrom(self):
        runCommand = commands.getstatusoutput
        output = runCommand('sudo python parseEmails.py sampleEmails.tar.gz "From"')
        self.assertEquals('A total of 12 matches were found! The result was output to emailSearchResults.txt.', (output[1].split('\n'))[1] )        
        timesFound = self.parseMessages('From')
        self.assertEquals(timesFound, 12)




if __name__ == '__main__':
    unittest.main()
