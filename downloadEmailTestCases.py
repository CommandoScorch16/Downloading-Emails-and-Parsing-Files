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
        os.chdir('downloadedEmails')
        output = commands.getstatusoutput('sudo rm *.txt')
        os.chdir('..')
        output = commands.getstatusoutput('sudo python downloadEmails.py \'subject:Czechoslovakia\'') 
        os.chdir('downloadedEmails')
        output = commands.getstatusoutput('ls')        
        output = output[1]
        commands.getstatusoutput('sudo rm \'Take a lovely holiday in Czechoslovakia!.txt\'')
        self.assertEqual(output, 'Take a lovely holiday in Czechoslovakia!.txt')




if __name__ == '__main__':
    unittest.main()
