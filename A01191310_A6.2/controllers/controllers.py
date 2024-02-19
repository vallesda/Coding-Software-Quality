import json
from models.models import Customer, Hotel, Reservation

class HotelController():
    """
        Controller class to manage, store, create, delete and update hotels
    """
    def __init__(self, filename):
        self.filename = filename
        self.hotels = self.load_data()

    def load_data(self):
        """Loads hotel data from file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return []
                hotels_data = json.load(file)
                hotels_list = []
                for hotel in hotels_data:
                    r = Hotel(hotel['name'],
                                    hotel['location'],
                                    hotel["phone"],
                                    hotel["available_rooms"])
                    hotels_list.append(r)
                return hotels_list
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON data in file")
            return []

    def save_data(self):
        """Saves hotel date to file"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            hotels_data = [
                 { 'name': hotel.name, 'location': hotel.location,
                  'phone': hotel.phone, 'available_rooms': hotel.available_rooms }
                for hotel in self.hotels]
            json.dump(hotels_data, file, indent=4)

    def create_hotel(self, name, phone, location, available_rooms):
        """Creates hotel and saves it on data file"""
        hotel = Hotel(name, location, phone, available_rooms)
        self.hotels.append(hotel)
        self.save_data()

    def delete_hotel(self, index):
        """Deletes Hotel data"""
        if 0 <= index < len(self.hotels):
            del self.hotels[index]
            self.save_data()

    def update_hotel(self, index, new_name=None, new_address=None, available_rooms=None):
        """Updates room by index"""
        if 0 <= index < len(self.hotels):
            hotel = self.hotels[index]
            if new_name:
                hotel.name = new_name
            if new_address:
                hotel.address = new_address
            if available_rooms:
                hotel.available_rooms = available_rooms
            self.save_data()
            return True
        return False

    def list_hotels(self):
        """Returns a list of hotels"""
        return self.hotels

    def display_hotel_information(self, index):
        """Returns a hotel information"""
        hotel = self.hotels[index]
        return hotel

    def reserve_room(self, index):
        """Reserves available rooms"""
        if self.hotels[index]:
            hotel = self.hotels[index]
            if hotel.available_rooms > 0:
                self.hotels[index].available_rooms = hotel.available_rooms - 1
                self.save_data()

    def release_room(self, index):
        """release available rooms"""
        if self.hotels[index]:
            hotel = self.hotels[index]
            if hotel.available_rooms > 0:
                self.hotels[index].available_rooms = hotel.available_rooms + 1
                self.save_data()

class CustomerController():
    """
        Controller class to manage, store, create, delete and update customer
    """
    def __init__(self, filename):
        self.filename = filename
        self.customers = self.load_data()

    def load_data(self):
        """Loads customer data from file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return []
                customer_data = json.load(file)
                customer_list = []
                for customer in customer_data:
                    r = Customer(customer['name'],
                                    customer['email'],
                                    customer["phone"],
                                    customer["reservation_history"])
                    customer_list.append(r)
                return customer_list
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON data in file")
            return []

    def save_data(self):
        """Saves customer date to file"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            customers_data = [
                 { 'name': customer.name, 'phone': customer.phone,
                  'email': customer.email, 'reservation_history': []  }
                for customer in self.customers]
            json.dump(customers_data, file, indent=4)

    def create_customer(self, name, phone, email):
        """Creates customer and saves it on data file"""
        customer = Customer(name, email, phone, [])
        self.customers.append(customer)
        self.save_data()

    def delete_customer(self, index):
        """Deletes customer data"""
        if 0 <= index < len(self.customers):
            del self.customers[index]
            self.save_data()

    def update_customer(self, index, new_name=None, new_email=None, new_phone=None):
        """Updates room by index"""
        if 0 <= index < len(self.customers):
            customer = self.customers[index]
            if new_name:
                customer.name = new_name
            if new_email:
                customer.email = new_email
            if new_phone:
                customer.phone = new_phone
            self.save_data()
            return True
        return False

    def list_customers(self):
        """Returns a list of customers"""
        print(self.customers)
        return self.customers

    def display_customer_information(self, index):
        """Returns a customer information"""
        customer = self.customers[index]
        print(customer)
        return customer

class ReservationController():
    """
        Controller class to manage, store, create, delete and update reservation
    """
    def __init__(self, filename):
        self.filename = filename
        self.reservations = self.load_data()

    def load_data(self):
        """Loads reservation data from file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return []
                reservation_data = json.load(file)
                res_list = []
                for rv in reservation_data:
                    r = Reservation(rv['customer_id'],
                                    rv['customer_hotel'],
                                    rv["start_day"],
                                    rv["end_day"])
                    res_list.append(r)
                return res_list
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.decoder.JSONDecodeError:
            print("Error decoding JSON data in file")
            return []

    def save_data(self):
        """Saves reservation date to file"""
        with open(self.filename, 'w', encoding='utf-8') as file:
            reservation_data = [
                 { 'customer_id': reservation.customer_id, 'hotel_id': reservation.hotel_id,
                  'start_day': reservation.start_day, 'end_day': reservation.end_day }
                for reservation in self.reservations]
            json.dump(reservation_data, file, indent=4)

    def create_reservation(self, customer_id, hotel_id, start_day, end_day):
        """Creates reservation and saves it on data file"""
        reservation = Reservation(customer_id, hotel_id, start_day, end_day)
        self.reservations.append(reservation)
        self.save_data()

    def delete_reservation(self, index):
        """Deletes reservation data"""
        if 0 <= index < len(self.reservations):
            del self.reservations[index]
            self.save_data()

    def update_reservation(self, index, new_start_day=None, new_end_day=None):
        """Updates room by index"""
        if 0 <= index < len(self.reservations):
            reservation = self.reservations[index]
            if new_start_day:
                reservation.start_day = new_start_day
            if new_end_day:
                reservation.start_end = new_end_day
            self.save_data()
            return True
        return False

    def list_reservations(self):
        """Returns a list of reservations"""
        print(self.reservations)
        return self.reservations

    def display_reservation_information(self, index):
        """Returns a reservation information"""
        reservation = self.reservations[index]
        print(reservation)
        return reservation
