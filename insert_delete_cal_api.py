from calendar import calendar
from pprint import pprint
from Google import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
request_body = {
    'summary':'calendars event'
}
"""
To create a calendar
"""
response = service.calendars().insert(body=request_body).execute()
print(response)

"""
To delete a calendar
"""
service.calendars().delete(calendarId='').execute()
# id:addressbook#contacts@group.v.calendar.google.com