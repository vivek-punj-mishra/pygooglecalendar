
from calendar import calendar
from pprint import pprint
from urllib import response
from Google import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# print(dir(service))
response = service.calendarList().list(
    maxResults=250,
    showDeleted=False,
    showHidden=False
    ).execute()
calendarItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.calendarList().list(
    maxResults=250,
    showDeleted=False,
    showHidden=False,
    pageToken=nextPageToken
    ).execute()
    calendarItems.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

print(calendarItems)    

# {
#   "kind": "calendar#calendarList",
#   "etag": etag,
#   "nextPageToken": string,
#   "nextSyncToken": string,
#   "items": [
#     calendarList Resource
#   ]
# }
# pprint(response)
# print(response.keys())
# print(response.get('items'))
# print(response.get('items')[0])
