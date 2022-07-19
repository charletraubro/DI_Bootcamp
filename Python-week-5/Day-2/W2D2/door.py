class Door:
    def __init__(self):
        self.is_opened = True
    
    def open(self):
        self.is_opened = True
        print("Door is opened")

    def close(self):
        self.is_opened = False
        print("Door is closed")

class BlockedDoor(Door):

    def __init__(self):
        self.is_opened = False
    
    def open(self):
        raise Exception("Cannot Open a Blocked DOOR!")

    def close(self):
        raise Exception("Cannot Close a Blocked DOOR!")


door = Door()

door.open()
door.close()

print(door.is_opened)

blocked_door = BlockedDoor()

blocked_door.open()
blocked_door.close()