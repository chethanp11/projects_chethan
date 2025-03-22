import math
from datetime import datetime, timedelta

class GeometryCalculator:
    def circle_area(self, radius: float) -> float:
        return math.pi * radius ** 2

    def circle_perimeter(self, radius: float) -> float:
        return 2 * math.pi * radius

    def rectangle_area(self, length: float, width: float) -> float:
        return length * width

    def rectangle_perimeter(self, length: float, width: float) -> float:
        return 2 * (length + width)

    def distance_between_points(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def triangle_area(self, base: float, height: float) -> float:
        return 0.5 * base * height

    def triangle_perimeter(self, a: float, b: float, c: float) -> float:
        return a + b + c

class ArithmeticCalculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class AstronomyCalculator:
    def utc_to_julian_date(self, utc_time: datetime) -> float:
        return utc_time.timestamp() / 86400.0 + 2440587.5

    def julian_date_to_utc(self, julian_date: float) -> datetime:
        timestamp = (julian_date - 2440587.5) * 86400.0
        return datetime.utcfromtimestamp(timestamp)

    def calculate_celestial_position(self, ra: float, dec: float, observer_lat: float, observer_lon: float) -> dict:
        return {"azimuth": 0.0, "altitude": 0.0}

    def convert_equatorial_to_horizontal(self, ra: float, dec: float, observer_lat: float, observer_lon: float, time: datetime) -> dict:
        return {"azimuth": 0.0, "altitude": 0.0}