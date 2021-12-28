from googleapiclient.discovery import build
from httplib2 import HttpLib2Error
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint


# https://cloud.google.com/channel/docs/codelabs/workspace/domain-verification#python

# Message data
json_payload = {
    "owner": ["liuchenggang@google.com",
              "cliu201-sa@cliu201.iam.gserviceaccount.com"
              ],
    "site": {
        "identifier": "run5.goodvm.net",
        "type": "INET_DOMAIN"
    }
}


def main():
    # Application default credentials are provided in Google API Client Libraries automatically.
    # You just have to build and initialize the API:

    service = build("siteVerification", "v1")

    try:
        lists = service.webResource().list().execute()
        pprint.pprint(lists)
        res = service.webResource().insert(
            verificationMethod="DNS_TXT", body=json_payload).execute()
        pprint.pprint(res)
    except HttpLib2Error as e:
        print('Error response status code : {0}, reason : {1}'.format(
            e.status_code, e.error_details))

    # service.close()


if __name__ == '__main__':
    main()
