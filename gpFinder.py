import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client.file import Storage
from oauth2client import tools

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class gpFinder:
    # If modifying these scopes, delete your previously saved credentials
    # at ~/.credentials/drive-python-quickstart.json
    SCOPES = 'https://www.googleapis.com/auth/drive.photos.readonly'
    CLIENT_SECRET_FILE = 'googleApi_secret.json'
    APPLICATION_NAME = 'Drive API Python Quickstart'

    def __init__(self):
        credentials = self._get_credentials()
        self._http = credentials.authorize(httplib2.Http())

    def _get_credentials(self):
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
                                       'drive-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def exists(self, file_name):
        service = discovery.build('drive', 'v3', http=self._http)
        results = service.files().list(
            pageSize=10,
            fields="nextPageToken, files(id, name)",
            q="name contains '" + file_name + "'",
            spaces="photos").execute()
        items = results.get('files', [])
        if not items:
            return False
        else:
            return True
