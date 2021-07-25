from heapq import heapify, heappush, heappop

class ParkingLot:
    def __init__(self):
        self.size = 0
        self.slot_to_ticket = {}
        self.number_to_slot = {}
        self.next_empty = []

    def create_parking_lot(self, N):
        '''
        Creates a parking lot for given number of slots.
        Creates a min heap to keep track of free slots.

        Parameters
        ----------
            N (int) : number of slots

        Returns
        -------
            bool : True in any case (assumption : N >= 0)
        '''

        self.size = N

        heapify(self.next_empty)
        for i in range(1, N + 1):
            heappush(self.next_empty, i)

        return True
    
    def park_vehicle(self, number, age):
        '''
        Park car with given vehicle registration number and age of the driver.
        Returns a slot in O(log(n)) time complexity.

        Parameters
        ----------
            number (str) : vehicle registration number
            age (int) : age of the driver

        Returns
        -------
            int : -1 if no slot available else a valid slot number
        '''

        if self.size == 0:
            return -1

        if len(self.next_empty) == 0:
            return -1

        slot = heappop(self.next_empty)
        self.slot_to_ticket[slot] = (number, age)
        self.number_to_slot[number] = slot

        return slot

    def vacate_slot(self, slot):
        '''
        Vacates the given slot from the parking lot in O(log(n)) time complexity.

        Parameters
        ----------
            slot (int) : slot number to be vacated

        Returns
        -------
            list : empty if slot is already vacant else [vehicle-number, driver-age]
        '''
      
        if slot not in self.slot_to_ticket.keys():
            return []

        heappush(self.next_empty, slot)
        number = self.slot_to_ticket[slot][0]
        age = self.slot_to_ticket[slot][1]
        del self.slot_to_ticket[slot]
        del self.number_to_slot[number]

        return [number, age]

    def get_slot_numbers_for_driver_of_age(self, age):
        '''
        Returns the slot numbers alloted to the driver of given age in O(n) time complexity.

        Parameters
        ----------
            age (int) : age of the driver

        Returns
        -------
            list : slot numbers alloted to driver of given age
        '''
        result = []

        for key, value in self.slot_to_ticket.items():
            if value[1] == age:
                result.append(key)

        return result

    def get_slot_number_for_car_with_number(self, number):
        '''
        Returns the slot number alloted to a vehicle of given number in O(1) time complexity.

        Parameters
        ----------
            number (str) : number of the vehicle

        Returns
        -------
            int : -1 if number is not present else a valid slot number
        '''

        if number not in self.number_to_slot.keys():
            return -1

        return self.number_to_slot[number]


    def get_vehicle_registration_number_for_driver_of_age(self, age):
        '''
        Returns the vehicle registration number(s) of the driver(s) of given age in O(n) time complexity.

        Parameters
        ----------
            age (int) : age of the driver

        Returns
        -------
            list : vehicle numbers of the drivers of given age
        '''
        
        result = []

        for key, value in self.slot_to_ticket.items():
            if value[1] == age:
                result.append(value[0])

        return result
