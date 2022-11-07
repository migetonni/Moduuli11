class vehicle:
    def __init__(self):
        self.speed = 0
        self.odometer = 0

    def accelerate(self):
      self.speed += 1



class car(vehicle):
    def __init__(self,name):
        super().__init__(name)
        self.gas_level = 30


    def accelerate(self):
       super().accelerate()
        self.speed += 5
        self.gas_level -1

class bike(vehicle):
    def __init__(self,gears,name):
        super().__init__(name)
        self.number_of_gears = gears

v1 = car("Rälicaar")
v1.accelerate()

v2 = bike("mankeli")
v2.accelerate()
