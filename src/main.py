import argparse
from src.parking import ParkingLot

def execute(arguments, parking_obj):
    '''
    Executes a given command

    Parameters
    ----------
        arguments (list) : a command in the form of list, for example, 'Leave 2' => ['Leave', 2].
        parking_obj (ParkingLot) : object of class ParkingLot.
    '''

    action = arguments[0]

    if action == 'Create_parking_lot':
        parking_obj.create_parking_lot(int(arguments[1]))
        print(f'Created parking of {arguments[1]} slots')

    elif action == 'Park':
        if arguments[2] != 'driver_age':
            print('Invalid command')
        else:
            slot = parking_obj.park_vehicle(arguments[1], int(arguments[3]))
            if slot == -1:
                print('Sorry, parking lot is full')
            else:
                print(f'Car with vehicle registration number "{arguments[1]}" has been parked at slot number {slot}')

    elif action == 'Leave':
        res = parking_obj.vacate_slot(int(arguments[1]))
        if len(res) == 0:
            print('Slot already vacant')
        else:
            print(f'Slot number {arguments[1]} vacated, the car with vehicle registration number {res[0]} left the space, the driver of the car was of age {res[1]}')

    elif action == 'Slot_numbers_for_driver_of_age':
        res = parking_obj.get_slot_numbers_for_driver_of_age(int(arguments[1]))
        print("null" if len(res) == 0 else (',').join([str(i) for i in res]))

    elif action == 'Slot_number_for_car_with_number':
        res = parking_obj.get_slot_number_for_car_with_number(arguments[1])
        if res == -1:
            print(f"No vehicle number found matching {arguments[1]}")
        else:
            print(res)

    elif action == 'Vehicle_registration_number_for_driver_of_age':
        res = parking_obj.get_vehicle_registration_number_for_driver_of_age(int(arguments[1]))
        print("null" if len(res) == 0 else (',').join(res))
        
    else:
        print('Invalid command')

def parking_service(parking_obj):
    '''
    Reads commands line by line directly from the input file and executes them.

    Parameters
    ----------
        parking_obj : ParkingLot
            empty object of class ParkingLot

    Raises
    ------
        Any Exception that occurs
    '''

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('input_file')
        args = parser.parse_args()

        if args.input_file:
            with open(args.input_file) as commands:
                for command in commands:
                    arguments = command.split()
                    execute(arguments, parking_obj)
    except Exception as e:
        print('Error: ' + str(e))

if __name__ == '__main__':
    parking_obj = ParkingLot()
    parking_service(parking_obj)
