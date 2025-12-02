class Dial:
    def __init__(self, init_location: int):
        self.location = init_location


    def turn(self,rotation: str) -> int:
        past_zero = 0
        if(rotation.startswith("L")):
            past_zero += self.slowTurnLeft(int(rotation[1:]))
        if(rotation.startswith("R")):
            past_zero += self.slowTurnRight(int(rotation[1:]))
        
        return past_zero

    def turnLeft(self,rotation: int):
        self.location  = (self.location  - rotation) % 100
        while (self.location < 0):
            self.location += 100
        return

    def turnRight(self, rotation: int):
        self.location += rotation
        while (self.location > 99):
            self.location -= 100
        return
    
    def slowTurnLeft(self,rotation:int) -> int:
        past_zero = 0
        for i in range(rotation):
            self.location -=1
            self.location = self.location % 100
            if self.location == 0:
                past_zero += 1
        return past_zero

    def slowTurnRight(self,rotation:int) -> int:
        past_zero = 0
        for i in range(rotation):
            self.location +=1
            self.location = self.location % 100
            if self.location == 0:
                past_zero += 1
        return past_zero