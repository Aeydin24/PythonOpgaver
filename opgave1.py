#Python Opgaver
import time
import datetime

class LED:

    def __init__(self):
        pass

    def TurnOn():
        print("Blink!")

    def TurnOff():
        print("The LED stopped blinking")
        
class DateTime:
    def getTime():
            return datetime.datetime.now()

    
class Robot:
    startTid = datetime.datetime
    slukTid = datetime.datetime
    
    def __init__(self, name = "Jørgen"):
        self.name = name
        print("Robot with name " + name + " has initialized")
        
    def turnOnRobot(self):
        time.sleep(1)
        self.startTid = DateTime.getTime()
        LED.TurnOn()
        print("Robot has turned on. Current time is: ", self.startTid,)
        
    def turnOffRobot(self):
        self.slukTid = DateTime.getTime()
        LED.TurnOff()
        print("Robot " + self.name + " has turned off. It was turned off at: ", datetime.datetime.now(), ", and stayed active for: ", self.slukTid - self.startTid )
        
tidinstance = DateTime()
l1 = LED()
r1 = Robot("Jørgen")
r1.turnOnRobot()
time.sleep(15)
r1.turnOffRobot()
