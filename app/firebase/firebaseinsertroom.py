from firebase import firebase


firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)

room_id = input(" Input you ID room :  ")
Type = input(" Input you Type room :  ")
name_room = input(" Input you Room name :  ")
Price = input(" Input Price of Room :  ")
engineer = {"Type of room": Type, "name_room": name_room, "Price": Price}


result = firebase.put("/Hotel_room", room_id, engineer)
