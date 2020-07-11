import requests
import datetime
import json

url_items = "http://localhost:3000/flows"
getResponse = requests.get(url_items)
id = len(getResponse.json())

newItem = {
    "id" : id,
    "time" : datetime.datetime.now(),
    "event" : "test_event"
}
response = requests.post(url_items, data=newItem)
# print(response.text)