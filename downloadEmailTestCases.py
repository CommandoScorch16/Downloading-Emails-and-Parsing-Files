import unittest
import commands
import os
class DownloadEmailTestMethods(unittest.TestCase):

    def test_ping(self):
        pingStatus = commands.getstatusoutput('ping google.com -c 1')
        internetStatus = 0
        if ('1 received' in str(pingStatus)):
            internetStatus = 1    
        self.assertEqual(internetStatus,1)
 
    def test_download(self):
        runCommand = commands.getstatusoutput
        os.chdir('downloadedEmails')
        runCommand('sudo rm *.txt')
        os.chdir('..')
        runCommand('sudo python downloadEmails.py \'subject:Czechoslovakia\'') 
        os.chdir('downloadedEmails')
        output = runCommand('ls')
        #Check for the file name in the tuple that got returned, to make sure we downloaded the one email, and ensure that is ALL we downloaded!   
        output = output[1]
        runCommand('sudo rm \'Take a lovely holiday in Czechoslovakia!.txt\'')
        self.assertEqual(output, 'Take a lovely holiday in Czechoslovakia!.txt')




if __name__ == '__main__':
    unittest.main()
