
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    
    def __init__(self, make, model, mpg, tank_capacity):
        '''Constructor for objects of type Car. Takes in four arguments:
            - make (a string, the company name, a.k.a. brand)
            - model (a string)
            - mpg (miles per gallon, a float)
            - tank_capacity (capacity of the gas tank in gallons, a float)'''
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    #   Getters for make, model, mpg, and tank_capacity.
    
    def get_make(self):
        '''Takes make as argument'''
        return self.__make
    
    def get_model(self):
        '''Takes model as argument'''
        return self.__model
    
    def get_mpg(self):
        '''Takes mpg (miles per gallon) as argument'''
        return self.__mpg
    
    def get_tank_capacity(self):
        '''Takes tank capacity (in gallons) as argument'''
        return self.__tank_capacity

    # Setters for mpg and tank_capacity.

    def set_mpg(self, mpg):
        '''Sets mpg using setter'''
        self.__mpg = mpg

    def set_tank_capacity(self, tank_capacity):
        '''Sets tank capacity using setter'''
        self.__tank_capacity = tank_capacity

    def get_total_range(self):
        '''Returns the total distance the car can travel on a full tank of gas'''
        return self.__tank_capacity * self.__mpg
        
        
    def __str__(self):
        '''A string for printing information about a car.'''
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) \
            + ', tank capacity: ' + str(self.__tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  

    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        '''Constructor for objects of type Car. Takes in four arguments:
            - make (a string, the company name, a.k.a. brand)
            - model (a string)
            - mpg (miles per gallon, a float)
            - tank_capacity (capacity of the gas tank in gallons, a float)
            - battery_kWh (battery power in kilowatt-hours, a float)
            - miles_per_kWh (miles per kilowatt-hours, a float)'''
        Car.__init__(self, make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

##    def get_battery_kWh(self):
##        '''Getter for battery power in kilowatt-hours'''
##        return self.__battery_kWh
##
##    def get_miles_per_kWh(self):
##        '''Getter for miles per kilo-watt hours'''
##        return self.__miles_per_kWh

    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.__battery_kWh * self.__miles_per_kWh
 
    def get_total_range(self):
        '''Overrides the method get_total_range in Car.
        Returns the total distance the car can travel on a full tank of
        gas and a fully charged battery.
        '''
        return Car.get_total_range(self) + self.get_battery_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.__battery_kWh) + ', miles/kWh: ' + \
            str(self.__miles_per_kWh)
