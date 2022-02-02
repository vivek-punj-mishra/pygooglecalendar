
from calendar import Calendar, calendar
from lib2to3.pytree import convert
from pprint import pprint
import re
from turtle import color
from urllib import response
from Google import convert_to_RFC_datetime, create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# print(dir(service))

Calendar_id_varanasi = "en.indian#holiday@group.v.calendar.google.com"

"""
Create an event
"""
colors = service.colors().get().execute()
pprint(colors)
recurrence = [
    'RRULE:FREQ=MONTHLY;COUNT=2'
]

hour_adjustment = -8
event_request_body = {
    'start':{
        'dateTime':convert_to_RFC_datetime(2022,2,10,12 + hour_adjustment,30),
        'timeZone':'India Standard Time'
    },
    'end':{
        'dateTime':convert_to_RFC_datetime(2022,2,10,14 + hour_adjustment,30),
        'timeZone':'India Standard Time'
    },
    'summary':'Family Lunch',
    'description':'Having lunch with the parents',
    'colorId':5,
    'status':'confirmed',
    'transparency':'opaque',
    'visibility':'private',
    'location':'Varanasi',
    'attachments': [
        {
            'fileUrl':'https://drive.google.com/file/d/1aY8dDqAyR4ePA660q5sNZOQEJx4gpVTB/view',
            'title':'Invitation letter Template in word Doc'
        }
    ],
        'attendees':[
            {
                'displayName':'vpm',
                'comment':'I enjoy coding',
                'email':'vivekpunjmishra2016@gmail.com',
                'optional':False,
                'orgnizer':True,
                'responseStatus':'accepted'
            }
        ],
        'recurrence':recurrence
    #     "creator": {
    #     "id": string,
    #     "email": string,
    #     "displayName": string,
    #     "self": boolean
    #   },
    #   "organizer": {
    #     "id": string,
    #     "email": string,
    #     "displayName": string,
    #     "self": boolean
    #   },
    }
maxAttendees = 5
sendNotification = True
sendUpdate = 'none'
supportsAttachement =  True
response = service.events().insert(
    calendarId=Calendar_id_varanasi,
    maxAttendees=maxAttendees,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdate,
    supportsAttachments=supportsAttachement,
    body=event_request_body
).execute()

pprint(response)

eventId = response['Id']

"""
Update an event
"""
start_dateTime:convert_to_RFC_datetime(2022,2,10,18 + hour_adjustment,30)
end_dateTime:convert_to_RFC_datetime(2022,2,10,20 + hour_adjustment,30)

response['start']['dateTime'] = start_dateTime
response['end']['dateTime'] = end_dateTime
response['summary'] = 'Family Dinner'
response['description'] = 'Having Family Dinner'
service.events().update(calendarId=Calendar_id_varanasi,
 eventId =eventId,
 body = response).execute()

"""
Delete an event
"""
service.events().delete(calendarId=Calendar_id_varanasi, eventId = eventId).execute()
