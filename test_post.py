import requests
import json

url_items = "http://localhost:3000/flows"
newItem = {
    "time" : "test_time",
    "event" : "test_event"
}
response = requests.post(url_items, data=newItem)
print(response.text)