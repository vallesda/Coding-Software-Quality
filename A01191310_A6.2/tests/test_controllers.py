import unittest
from controllers.controllers import CustomerController, HotelController, ReservationController
from models.models import Customer, Hotel, Reservation

class TestReservationController(unittest.TestCase):
    """Tests controller class"""
    def setUp(self):
        self.test_file = 'test_reservations.json'
        self.controller = ReservationController(self.test_file)
        self.test_reservations = [
            Reservation(0, 0, "2024-02-18", "2024-02-21"),
            Reservation(1, 1, "2024-02-18", "2024-02-22")
        ]
        self.controller.reservations = self.test_reservations

    def test_create_reservation(self):
        """Tests reservation creation"""
        self.controller.create_reservation(0, 1, "2024-02-18", "2024-02-20")
        reservations = self.controller.load_data()
        self.assertEqual(len(reservations), 3)

    def test_list_reservations(self):
        """Tests lists of reservations"""
        reservations = self.controller.list_reservations()
        self.assertEqual(len(reservations), 2)
        self.assertEqual(reservations[0].customer_id, 0)
        self.assertEqual(reservations[1].hotel_id, 1)

    def test_update_reservation(self):
        """Tests update a reservation"""
        self.assertTrue(self.controller.update_reservation(0, new_end_day="2024-02-22"))
        reservations = self.controller.load_data()
        self.assertEqual(reservations[0].end_day, "2024-02-22")

class TestCustomerController(unittest.TestCase):
    """Tests controller class"""
    def setUp(self):
        self.test_file = 'test_customers.json'
        self.controller = CustomerController(self.test_file)
        self.test_customers = [
            Customer("Juan", "juan@gmail.com", "11112222", []),
            Customer("Julian", "julian@gmail.com", "222233333", [])
        ]
        self.controller.customers = self.test_customers

    def test_create_customer(self):
        """Tests customer creation"""
        self.controller.create_customer("Jorge", "jorge@gmail.com", "11118888")
        customers = self.controller.load_data()
        self.assertEqual(len(customers), 3)

    def test_list_customers(self):
        """Tests lists of customers"""
        customers = self.controller.list_customers()
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0].name, "Juan")
        self.assertEqual(customers[1].email, "julian@gmail.com")

    def test_update_customer(self):
        """Tests update a customer"""
        self.assertTrue(self.controller.update_customer(0, new_name="Aldo"))
        customers = self.controller.load_data()
        self.assertEqual(customers[0].name, "Aldo")


class TestHotelController(unittest.TestCase):
    """Tests controller class"""
    def setUp(self):
        self.test_file = 'test_hotels.json'
        self.controller = HotelController(self.test_file)
        self.test_hotels = [
            Hotel("Hotel A", "Guadalajara", "11112222", 50),
            Hotel("Hotel B", "Mexico", "33338888", 100)
        ]
        self.controller.hotels = self.test_hotels

    def test_create_hotel(self):
        """Tests hotel creation"""
        self.controller.create_hotel("Hotel C", "Monterrey", "44445555", 150)
        hotels = self.controller.load_data()
        self.assertEqual(len(hotels), 3)

    def test_list_hotels(self):
        """Tests lists of hotels"""
        hotels = self.controller.list_hotels()
        print(hotels)
        self.assertEqual(len(hotels), 2)
        self.assertEqual(hotels[0].name, "Hotel A")
        self.assertEqual(hotels[1].available_rooms, 100)

    def test_update_hotel(self):
        """Tests update a hotel"""
        self.assertTrue(self.controller.update_hotel(0, new_name="Hotel X"))
        hotels = self.controller.load_data()
        self.assertEqual(hotels[0].name, "Hotel X")

if __name__ == '__main__':
    unittest.main()
