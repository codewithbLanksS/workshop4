from firebase import firebase

id = input(" Input ID if you want to DELETE :  ")

firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)

firebase.delete("/Hotel_room", id)
