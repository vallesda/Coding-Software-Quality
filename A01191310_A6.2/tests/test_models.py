import unittest
from models.models import Customer, Hotel, Reservation

class TestHotel(unittest.TestCase):
    """Tests hotel models"""
    def setUp(self):
        self.hotel = Hotel("House Hotel", "Monterrey", "83568899", 50)

    def test_hotel_creation(self):
        """Tests model class creation of hotels"""
        self.assertEqual(self.hotel.name, "House Hotel")
        self.assertEqual(self.hotel.phone, "83568899")
        self.assertEqual(self.hotel.location, "Monterrey")
        self.assertEqual(self.hotel.available_rooms, 50)

    def test_invalid_availability(self):
        """Tests for invalid availability of rooms"""
        with self.assertRaises(ValueError):
            Hotel("House Hotel", "Monterrey", "83568899", -50)

    def test_invalid_name(self):
        """Tests for invalid name"""
        with self.assertRaises(ValueError):
            Hotel(10, "Monterrey", "83568899", 50)

    def test_invalid_location(self):
        """Tests for invalid location"""
        with self.assertRaises(ValueError):
            Hotel("House Hotel", 50, "83568899", 50)

    def test_invalid_phone(self):
        """Tests for invalid phone"""
        with self.assertRaises(ValueError):
            Hotel("House Hotel", "Monterrey", 83568899, 50)

class TestCustomer(unittest.TestCase):
    """Tests customer models"""
    def setUp(self):
        self.customer = Customer("Jose", "jose@gmail.com", "84569988", [])

    def test_customer_creation(self):
        """Tests model class creation of customers"""
        self.assertEqual(self.customer.name, "Jose")
        self.assertEqual(self.customer.email, "jose@gmail.com")
        self.assertEqual(self.customer.phone, "84569988")

    def test_invalid_name(self):
        """Tests for invalid name"""
        with self.assertRaises(ValueError):
            Customer(12, "jose@gmail.com", "84569988", [])

    def test_invalid_phone(self):
        """Tests for invalid phone number"""
        with self.assertRaises(ValueError):
            Customer("Jose", "jose@gmail.com", 84271929, [])

    def test_invalid_email(self):
        """Tests for invalid email"""
        with self.assertRaises(ValueError):
            Customer("Jose", 1, "84271929", [])

class TestReservation(unittest.TestCase):
    """Tests model reservation"""
    def setUp(self):
        self.reservation = Reservation(0, 1, "2024-02-18", "2024-02-20")

    def test_reservation_creation(self):
        """Test reservation creation"""
        self.assertEqual(self.reservation.customer_id, 0)
        self.assertEqual(self.reservation.hotel_id, 1)
        self.assertEqual(self.reservation.start_day, "2024-02-18")
        self.assertEqual(self.reservation.end_day, "2024-02-20")

    def test_invalid_id(self):
        """Tests for invalid ids"""
        with self.assertRaises(ValueError):
            Reservation(0, "1", "2024-02-18", "2024-02-20")

    def test_invalid_dates(self):
        """Tests for invalid dates"""
        with self.assertRaises(ValueError):
            Reservation(0, 1, "2024-02-18", 20240220)

if __name__ == '__main__':
    unittest.main()
