# Parking Lot Problem Solution
A simple implementation of parking lot problem in Python.

## Dependencies
Python 3.9 and above. Visit this [link](https://www.python.org/downloads/) to install python.

## Description
### Source code (src/)
```main.py``` processes and executes the input from the file. It implements the following functions:
```
parking_service(parking_obj) : reads commands line by line directly from input file and executes them
execute(arguments, parking_obj) : executes a given command
```

```parking.py``` contains a class - ```ParkingLot``` which implements the following functions:
```
create_parking_lot(N) :
- creates a parking lot of given size N
- returns True always (assumption N >= 0)

park_vehicle(number, age) : 
- parks a vehicle with given registration number belong to a driver of given age
- returns a valid slot number if there is an empty slot available
- returns -1 if vehicle cannot be parked
- time complexity : O(log(n))

vacate_slot(slot) :
- vacates the vehicle at given slot number if present 
- returns a list of the form [vehicle number, slot]
- returns empty list if slot is already vacant
- time complexity : O(log(n))

get_slot_numbers_for_drivers_of_age(age) :
- returns a list of slot number(s) alloted to the driver(s) of given age
- time complexity : O(n)

get_slot_number_for_car_with_number(number) : 
- returns the slot number alloted to a vehicle of given number
- return -1 if the given vehicle number is not present
- time complexity : O(1)

get_vehicle_registration_number_for_driver_of_age(age) : 
- returns the vehicle registration number(s) of the driver(s) of given age
- time complexity : O(n)
```

### Standard output format
```
----------------------------------------------------------------------------------------------------------------------------------
                 COMMAND                            |                 FORMAT
----------------------------------------------------------------------------------------------------------------------------------
Create_parking_lot <number-of-slots>                |  Created parking of <number-of-slots> slots
----------------------------------------------------------------------------------------------------------------------------------
Park <vehicle-number> driver_age <age>              |  
If an empty slot is available                       |  Car with vehicle registration number "<vehicle-number>" has been parked
                                                    |  at slot number <slot-number>
If no slot is available                             |  Sorry, parking lot is full
----------------------------------------------------------------------------------------------------------------------------------
Leave <slot-number>                                 |
If the given slot number is occupied                |  Slot number <slot-number> vacated, the car with vehicle registration number
                                                    |  <vehicle-number> left the space, the driver of the car was of age <age>
If the slot is already vacant                       |  Slot already vacant 
-----------------------------------------------------------------------------------------------------------------------------------
Slot_numbers_for_driver_of_age <age>                |  [slot-1, slot-2, ..., slot-N
If empty                                            |  null
-----------------------------------------------------------------------------------------------------------------------------------
Slot_number_for_car_with_number <vehicle-number>    |
If vehicle is present                               |  Car with vehicle registration number <vehicle-number> has been parked at 
                                                    |  slot number <slot-number> 
If vehicle is not present                           |  No vehicle number found matching <vehicle-number>
-----------------------------------------------------------------------------------------------------------------------------------
Vehicle_registration_number_for_driver_of_age <age> |  [vehicle-number-1, vehicle-number-2,...,vehicle-number-N]
If empty                                            |  null
-----------------------------------------------------------------------------------------------------------------------------------
```
### Sample input and Output
#### Input (from file present on local system)
```
Create_parking_lot 6
Park KA-01-HH-1234 driver_age 21
Park PB-01-HH-1234 driver_age 21
Slot_numbers_for_driver_of_age 21
Park PB-01-TG-2341 driver_age 40
Slot_number_for_car_with_number PB-01-HH-1234
Leave 2
Park HR-29-TG-3098 driver_age 39
Vehicle_registration_number_for_driver_of_age 18
```

#### Output (on terminal)
```
Created parking of 6 slots
Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
1,2
Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
2
Slot number 2 vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21
Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
null
```

## Run
```
~$ git clone https://github.com/shivamacs/parking-lot-problem.git
~$ cd parking-lot-problem
~/parking-lot-problem$ python -m src.main <input-file-path>
```
To run ```sample_input.txt```, present in this repository
```
~/parking-lot-problem$ python -m src.main sample_input.txt 
```
or
```
~/parking-lot-problem$ python3 -m src.main sample_input.txt 
```

### Tests
There are 6 tests written to test all the functions of class ```ParkingLot```. To run the test file:
```
~/parking-lot-problem$ python -m unittest tests.test
```
or
```
~/parking-lot-problem$ python3 -m unittest tests.test
```
which produces the following output:
```
......
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
