
class Robot:
    def __init__(self,name,battery_level):
        self.name=name
        self.set_batteryLevel(battery_level)

    def set_batteryLevel(self,battery_level):
        if battery_level>=0 and battery_level<=100:
         self.__battery_level=battery_level
        else:
           print("battery level must be within range")

    def get_batteryLevel(self):
        return self.__battery_level

    def status(self):
      return f"{self.name}, Battery level: {self.get_batteryLevel()} %"
    # def move(self):
    #     ...


class GroundRobot(Robot):
    def __init__(self, name, battery_level,wheels):
        super().__init__(name, battery_level)
        self.wheels=wheels
    def move(self):
        return f"{self.name} is moving on {self.wheels} wheels"



class AerialRobot(Robot):
    def __init__(self, name, battery_level,rotors):
        super().__init__(name,battery_level)
        self.rotors=rotors
    def move(self):
        return f"{self.name} is flying with {self.rotors} rotors"

class fleetMangament:
   def __init__(self):
      self.robots=[]

   def add_robot(self,robot):
      if isinstance(robot,Robot):
         self.robots.append(robot)
      else:
         print("can only add robots to the fleet")
   def statusOfAll(self):
      for robot in self.robots:
         print(robot.status())
   def movementOfAll(self):
        for robot in self.robots:
         print(robot.move())

      

def main():
 myfleet=fleetMangament()
 robot1=AerialRobot("AirBot",90,4)
 robot2=GroundRobot("GroundBot",68,6)
 myfleet.add_robot(robot1)
 myfleet.add_robot(robot2)
 myfleet.movementOfAll()
 myfleet.statusOfAll()
 

main()