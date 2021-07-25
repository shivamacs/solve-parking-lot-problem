import unittest
from src.parking import ParkingLot

class TestParkingLot(unittest.TestCase):
	'''
	Tests all functions of class ParkingLot
	'''
	def test_create_parking_lot(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		self.assertEqual(True, res)

	def test_park_vehicle(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		res = parkingLot.park_vehicle("KA-01-HH-1234", 21)
		self.assertEqual(1, res)

	def test_vacate_slot(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		res = parkingLot.park_vehicle("KA-01-HH-1234", 21)
		res = parkingLot.vacate_slot(1)
		self.assertIn("KA-01-HH-1234", res)
		self.assertIn(21, res)

	def test_get_slot_numbers_for_driver_of_age(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		res = parkingLot.park_vehicle("KA-01-HH-1234", 21)
		res = parkingLot.park_vehicle("PB-01-HH-1234", 21)
		slot_nums = parkingLot.get_slot_numbers_for_driver_of_age(21)
		self.assertIn(1, slot_nums)
		self.assertIn(2, slot_nums)

	def test_get_slot_number_for_car_with_number(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		res = parkingLot.park_vehicle("KA-01-HH-1234", 21)
		res = parkingLot.park_vehicle("PB-01-HH-1234", 21)
		slotno = parkingLot.get_slot_number_for_car_with_number("PB-01-HH-1234")
		self.assertEqual(2, slotno)

	def test_get_vehicle_registration_number_for_driver_of_age(self):
		parkingLot = ParkingLot()
		res = parkingLot.create_parking_lot(6)
		res = parkingLot.park_vehicle("KA-01-HH-1234", 21)
		res = parkingLot.park_vehicle("PB-01-HH-1234", 21)
		vehicle_nums = parkingLot.get_vehicle_registration_number_for_driver_of_age(21)
		self.assertIn("KA-01-HH-1234", vehicle_nums)
		self.assertIn("PB-01-HH-1234", vehicle_nums)

if __name__ == '__main__':
	unittest.main()