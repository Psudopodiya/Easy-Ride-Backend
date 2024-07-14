from decimal import Decimal
from django.core.management.base import BaseCommand
from cars.models import Car, Brand
import random

class Command(BaseCommand):
    help = 'Seeds the database with realistic car and brand data'

    def handle(self, *args, **kwargs):
        car_data = [
            ("Toyota", ["Camry", "Corolla", "RAV4", "Prius", "Highlander"]),
            ("Honda", ["Civic", "Accord", "CR-V", "Pilot", "Odyssey"]),
            ("Ford", ["F-150", "Mustang", "Explorer", "Escape", "Focus"]),
            ("Chevrolet", ["Silverado", "Equinox", "Malibu", "Traverse", "Camaro"]),
            ("Nissan", ["Altima", "Rogue", "Sentra", "Maxima", "Pathfinder"]),
            ("BMW", ["3 Series", "5 Series", "X3", "X5", "7 Series"]),
            ("Mercedes-Benz", ["C-Class", "E-Class", "GLC", "S-Class", "GLE"]),
            ("Volkswagen", ["Jetta", "Passat", "Tiguan", "Atlas", "Golf"]),
            ("Audi", ["A4", "Q5", "A6", "Q7", "A3"]),
            ("Hyundai", ["Elantra", "Sonata", "Tucson", "Santa Fe", "Kona"])
        ]

        basic_features = [
            {"Transmission": "Automatic", "Seats": "5 Seats", "Mileage": "30 MPG", "Drive Type": "FWD",
             "Engine Type": "Petrol", "Fuel Tank Capacity": "15 gallons"},
            {"Transmission": "Automatic", "Seats": "7 Seats", "Mileage": "25 MPG", "Drive Type": "AWD",
             "Engine Type": "Hybrid", "Fuel Tank Capacity": "18 gallons"},
            {"Transmission": "Manual", "Seats": "4 Seats", "Mileage": "35 MPG", "Drive Type": "RWD",
             "Engine Type": "Electric", "Fuel Tank Capacity": "N/A"},
            {"Transmission": "Automatic", "Seats": "5 Seats", "Mileage": "28 MPG", "Drive Type": "4WD",
             "Engine Type": "Diesel", "Fuel Tank Capacity": "20 gallons"},
            {"Transmission": "Automatic", "Seats": "5 Seats", "Mileage": "32 MPG", "Drive Type": "FWD",
             "Engine Type": "Petrol", "Fuel Tank Capacity": "17 gallons"}
        ]

        additional_features = [
            {"Roof": "Sunroof", "Connectivity": "Bluetooth", "Safety Features": "Collision Warning",
             "Interior Features": "Leather Seats", "Entertainment": "Touchscreen Display",
             "Climate Control": "Dual Zone"},
            {"Roof": "Panoramic", "Connectivity": "Wi-Fi", "Safety Features": "Lane Departure Warning",
             "Interior Features": "Heated Seats", "Entertainment": "Premium Sound System",
             "Climate Control": "Automatic"},
            {"Roof": "Standard", "Connectivity": "Apple CarPlay", "Safety Features": "Blind Spot Monitoring",
             "Interior Features": "Power Seats", "Entertainment": "Satellite Radio",
             "Climate Control": "Manual"},
            {"Roof": "Moonroof", "Connectivity": "Android Auto", "Safety Features": "Adaptive Cruise Control",
             "Interior Features": "Ventilated Seats", "Entertainment": "Rear Seat Entertainment",
             "Climate Control": "Tri-Zone"},
            {"Roof": "Fixed Glass", "Connectivity": "USB Ports", "Safety Features": "360-Degree Camera",
             "Interior Features": "Ambient Lighting", "Entertainment": "Wireless Charging",
             "Climate Control": "Single Zone"}
        ]

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Car.objects.all().delete()
        Brand.objects.all().delete()

        # Create brands and cars
        for brand_name, car_models in car_data:
            self.stdout.write(f'Creating {brand_name} brand and its models...')
            brand = Brand.objects.create(name=brand_name, country_of_origin="Unknown")

            for car_name in car_models:
                Car.objects.create(
                    name=car_name,
                    brand=brand,
                    rental_rate=Decimal(random.uniform(50.00, 200.00)).quantize(Decimal("0.01")),
                    car_class=random.choice(["Economy", "Midsize", "Luxury", "SUV", "Sports"]),
                    basic_features=random.choice(basic_features),
                    additional_features=random.choice(additional_features),
                    year_of_manufacturing=random.randint(2018, 2023),
                    rating=Decimal(random.uniform(3.5, 5.0)).quantize(Decimal("0.1")),
                    is_booked=random.choice([True, False])
                )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with realistic car data'))