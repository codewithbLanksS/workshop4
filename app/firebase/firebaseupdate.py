from firebase import firebase


firebase = firebase.FirebaseApplication(
    "https://sleepyhotelzoo-default-rtdb.firebaseio.com/", None
)


room_id = input(" Input you ID room :  ")

types = input("input you type for update :")
name = input("input you name of room for update :")
price = input("input you price for update : ")
firebase.put(f"Hotel_room/{room_id}", "Price", price)
firebase.put(f"Hotel_room/{room_id}", "Type of room", types)
firebase.put(f"Hotel_room/{room_id}", "name_room", name)

print("Record Updated")
