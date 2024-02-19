import uuid

class Hotel():
    """
    Represents a hotel
    
    Attributes:
        id(uuid): identification number
        name(string): name of hotel
        phone(string): phone number of hotel
        location(string): location by state
        available_rooms(int): capacity

    """
    def __init__(self, name, location, phone, available_rooms):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(location, str):
            raise ValueError("Location must be a string.")
        if not isinstance(phone, str):
            raise ValueError("Phone must be a string.")
        if not isinstance(available_rooms, int) or available_rooms < 0:
            raise ValueError("Available rooms should be int and positive")
        self.id = uuid.uuid4()
        self.name = name
        self.phone = phone
        self.location = location
        self.available_rooms = available_rooms

class Customer():
    """
    Represents a Customer
    
    Attributes:
        id(uuid): Identification of Customer
        name(string): Name of customer
        email(string): email of customer
        phone(string): phone number of customer
        reservation_history(reservations): list of reservations
    """
    def __init__(self, name, email,  phone, reservation_history):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(email, str):
            raise ValueError("Email must be a string.")
        if '@' not in email:
            raise ValueError("Invalid email address.")
        if not isinstance(phone, str):
            raise ValueError("Phone must be a string.")
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone = phone
        self.reservation_history = reservation_history

class Reservation():
    """
    Represents a reservation between a hotel and a customer

    Attributes:
        id(uuid): identification of reservation
        customer_id(int): id of customer
        hotel_id(int): id of hotel
        start_day:(string)
        end_day(string)
    """
    def __init__(self, customer_id, hotel_id, start_day, end_day):
        if (not isinstance(customer_id, int) or customer_id < 0 or
            not isinstance(hotel_id, int) or hotel_id < 0):
            raise ValueError("Ids should be integers")
        if not isinstance(start_day, str) or not isinstance(end_day, str):
            raise ValueError("dates should be strings.")
        self.id = uuid.uuid4()
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.start_day = start_day
        self.end_day = end_day
