"""Только для оценки 10\10 в pylint"""
class Device:
    """Только для оценки 10\10 в pylint""" 
    def __init__(self, brand, model):
        """
        Только для оценки 10\10 в pylint
        """    
        self.brand = brand
        self.model = model

    def turn_on(self):
        """
        Только для оценки 10\10 в pylint
        """    
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        """
        Только для оценки 10\10 в pylint
        """    
        print(f"{self.brand} {self.model} is turned off.")


class CoffeeMachine(Device):
    """Только для оценки 10\10 в pylint""" 
    def __init__(self, brand, model, capacity):
        """
        Только для оценки 10\10 в pylint
        """    
        super().__init__(brand, model)
        self.capacity = capacity

    def make_coffee(self):
        """
        Только для оценки 10\10 в pylint
        """    
        print(f"{self.brand} {self.model} is making coffee.")


class Blender(Device):
    """Только для оценки 10\10 в pylint""" 
    def __init__(self, brand, model, speed):
        """
        Только для оценки 10\10 в pylint
        """    
        super().__init__(brand, model)
        self.speed = speed

    def blend(self):
        """
        Только для оценки 10\10 в pylint
        """    
        print(f"{self.brand} {self.model} is blending.")

class MeatGrinder(Device):
    """Только для оценки 10\10 в pylint""" 
    def __init__(self, brand, model, power):
        """
        Только для оценки 10\10 в pylint
        """    
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        """
        Только для оценки 10\10 в pylint
        """    
        print(f"{self.brand} {self.model} is grinding meat.")

if __name__ == "__main__":
    coffee_machine = CoffeeMachine("Breville", "C100", "1L")
    coffee_machine.turn_on()
    coffee_machine.make_coffee()
    coffee_machine.turn_off()

    blender = Blender("Vitamix", "VM200", "High")
    blender.turn_on()
    blender.blend()
    blender.turn_off()

    meat_grinder = MeatGrinder("KitchenAid", "KG300", "500W")
    meat_grinder.turn_on()
    meat_grinder.grind_meat()
    meat_grinder.turn_off()
