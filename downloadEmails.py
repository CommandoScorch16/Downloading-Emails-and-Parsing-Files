# Samuel Horton
# Downloading Emails from Gmail
# January 10th, 2017
# In order to use the GMAIL API, I used code from the official Guide here:
# https://developers.google.com/gmail/api/quickstart/python

from __future__ import print_function
import httplib2
import os

from apiclient import discovery, errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def getMessageIdsThatMatchQuery(service, user_id, query):
    """Gets the message Ids of every message that matches the query.
    """
    try:
        response = service.users().messages().list(userId=user_id,q=query).execute()
        messages = []
        if 'messages' in response:
            numberOfMatches = response['resultSizeEstimate']
            print('%s messages were found that matched the query, downloading them now!' % numberOfMatches)
            messages.extend(response['messages'])
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
            messages.extend(response['messages'])
        if (len(messages) > 0):
            for message in messages:
                getMessageThatMatchesQuery(service, user_id, message['id'])
        else:
            print('ERROR: No messages were found by the query %s' % query)
        
    except errors.HttpError, error:
        print ('An error has occured: %s' % error)

def getMessageThatMatchesQuery(service, user_id, message_id):
    try:
        message = service.users().messages().get(userId=user_id, id=message_id).execute()
        if len(message) > 0:
            # Now get the email subject out of this nest of lists and dictionaries
            messageHeaders = message['payload']['headers']
            # 3 is getting subtracted from the length, because the dictionary that contains the
            # subject is two behind the last dictionary in the list
            messageSubject = messageHeaders[(len(message['payload']['headers'])-3)]
            messageSubject = messageSubject['value']
            # Now write the message to a text file, and name it the subject of the message
            emailFile = open(('%s.txt' % messageSubject), 'w')
            emailFile.write(str(message))
            emailFile.close()
        else:
            print('ERROR: No message could be found with with message_id')

    except errors.HttpError, error:
        print ('An error occurred: %s' % error)

def main():
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    #Change directory into the subfolder so we don't pollute this directory with text files that have long names!
    os.chdir("downloadedEmails")
    # 'me' is just slang for the current authenticated user's gmail account, or in this case, returnpath.isawesome@gmail.com
    # This is a literal GMAIL query string, you could copy and paste it into the GMAIL search bar and it would also filter correctly!
    getMessageIdsThatMatchQuery(service, 'me', 'subject:Netflix OR subject:"Home Depot" OR subject:1800flowers')
          


if __name__ == '__main__':
    main()
