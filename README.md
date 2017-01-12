#Part 1
#Downloading Emails
##To run downloadEmails.py, you need the following dependencies:
###1. A Linux based operating system that has access to 'pip' and an internet browser
###2. An internet connection
###3. Python 2.6 or newer

##Once these are good to go, type the command ``pip install --upgrade google-api-python-client`` in the terminal
##After this has finished installing, you can the following command (It will need to have write privileges for the emails once they have been downloaded)
##``sudo python downloadEmails.py``
##It should open up a browser, and ask you to login with your GMAIL account
##``Email: returnpath.isawesome@gmail.com``
##``Password: testTEST``
##Once you have logged in successfully, you will want to run the following command:
##``sudo python downloadEmails.py 'subject:Netflix OR subject:"Home Depot" OR subject:1800flowers'``
##This will now download emails because you now have the correct credentials
##Once this has finished, you can run the command 'cd downloadedEmails' to go into the directory where all of the downloaded emails exist
##Now you can type ``ls -l`` to make it easier to see them
##It is worth noting that each email contains all of the metadata, such as the time it was sent, and who sent it. This information can be used for later parsing

#Running the test cases for Part 1
##To run the test cases, type the command ``sudo python downloadEmailTestCases.py`` 


#Part 2
#Parsing Emails
##To run parseEmails.py, you need the following dependencies:
###1. A Linux based operating system
###2. A running Python installation

##When you have both of these things ready, type the command ``sudo python parseEmails.py name_of_tarfile "parameter 1" "parameter 2"...``
##Where nameoftarfile is name of the file to be extracted, and parameter 1, parameter 2,... are the names of fields you want to search for in the email, like "subject" or "from" or "content-type"
##When you run this, it will output everything into one file, named ``emailSearchResults.txt``. In that file, it will show you the comma seperated matches divided up into sections, one for each email.

#Running the test cases for Part 2
##To run the test cases, type the command ``sudo python parseEmailTestCases.py``
