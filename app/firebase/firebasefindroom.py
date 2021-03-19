import json
from firebase import firebase

room_id = input(" Input you ID room you want to see:  ")
firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)


result = firebase.get("/Hotel_room", room_id)
print(result)
