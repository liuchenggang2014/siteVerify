from googleapiclient.discovery import build
from httplib2 import HttpLib2Error
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint




def main():
    # Application default credentials are provided in Google API Client Libraries automatically.
    # You just have to build and initialize the API:

    service = build("siteVerification", "v1")

    try:
        lists = service.webResource().list().execute()
        pprint.pprint(lists)
        pprint.pprint('**************************************')

    except HttpLib2Error as e:
        print('Error response status code : {0}, reason : {1}'.format(
            e.status_code, e.error_details))


if __name__ == '__main__':
    main()
