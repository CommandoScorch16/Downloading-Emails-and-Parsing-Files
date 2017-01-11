#Part 1
#Downloading Emails
##To run downloadEmails.py, you need the following dependencies:
###1. A Linux based operating system that has access to 'pip' and an internet browser
###2. An internet connection
###3. Python 2.6 or newer

##Once these are good to go, type the command 'pip install --upgrade google-api-python-client' in the terminal
##After this has finished installing, you can run 'sudo python downloadEmails.py' (It will need to have write privileges for the emails once they have been downloaded)
##It should open up a browser, and ask you to login with your GMAIL account
##Email: returnpath.isawesome@gmail.com
##Password: testTEST
##Once you have logged in successfully, you will want to run the following command:
##``sudo python downloadEmails.py 'subject:Netflix OR subject:"Home Depot" OR subject:1800flowers'``
##This will now download emails because you now have the correct credentials
##Once this has finished, you can run the command 'cd downloadedEmails' to go into the directory where all of the downloaded emails exist
##Now you can type 'ls -l' to make it easier to see them
##It is worth noting that each email contains all of the metadata, such as the time it was sent, and who sent it. This information can be used for later parsing

#Part 2
#
