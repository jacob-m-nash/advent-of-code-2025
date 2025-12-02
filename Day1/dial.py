class Dial:
    def __init__(self, init_location: int):
        self.location = init_location


    def turn(self,rotation: str):
        if(rotation.startswith("L")):
            self.turnLeft(int(rotation[1:]))
        if(rotation.startswith("R")):
            self.turnRight(int(rotation[1:]))
        
        return

    def turnLeft(self,rotation: int):
        self.location -= rotation
        while (self.location < 0):
            self.location += 100
        return

    def turnRight(self, rotation: int):
        self.location += rotation
        while (self.location > 99):
            self.location -= 100
        return