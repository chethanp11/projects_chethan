```python
import unittest
from datetime import datetime
from main_calculator import GeometryCalculator, ArithmeticCalculator, AstronomyCalculator

class TestGeometryCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = GeometryCalculator()

    def test_circle_area(self):
        self.assertAlmostEqual(self.calc.circle_area(0), 0)
        self.assertAlmostEqual(self.calc.circle_area(1), math.pi)
        self.assertAlmostEqual(self.calc.circle_area(2.5), math.pi * 2.5 ** 2)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(self.calc.circle_perimeter(0), 0)
        self.assertAlmostEqual(self.calc.circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(self.calc.circle_perimeter(2.5), 2 * math.pi * 2.5)

    def test_rectangle_area(self):
        self.assertEqual(self.calc.rectangle_area(0, 5), 0)
        self.assertEqual(self.calc.rectangle_area(5, 0), 0)
        self.assertEqual(self.calc.rectangle_area(3, 4), 12)

    def test_rectangle_perimeter(self):
        self.assertEqual(self.calc.rectangle_perimeter(0, 5), 10)
        self.assertEqual(self.calc.rectangle_perimeter(5, 0), 10)
        self.assertEqual(self.calc.rectangle_perimeter(3, 4), 14)

    def test_distance_between_points(self):
        self.assertEqual(self.calc.distance_between_points(0, 0, 0, 0), 0)
        self.assertEqual(self.calc.distance_between_points(0, 0, 3, 4), 5)

    def test_triangle_area(self):
        self.assertEqual(self.calc.triangle_area(0, 5), 0)
        self.assertEqual(self.calc.triangle_area(5, 0), 0)
        self.assertEqual(self.calc.triangle_area(3, 4), 6)

    def test_triangle_perimeter(self):
        self.assertEqual(self.calc.triangle_perimeter(0, 0, 0), 0)
        self.assertEqual(self.calc.triangle_perimeter(3, 4, 5), 12)

class TestArithmeticCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = ArithmeticCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(1, 0)

class TestAstronomyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = AstronomyCalculator()

    def test_utc_to_julian_date(self):
        self.assertAlmostEqual(self.calc.utc_to_julian_date(datetime(1970, 1, 1)), 2440587.5)
        self.assertAlmostEqual(self.calc.utc_to_julian_date(datetime(2000, 1, 1, 12)), 2451545.0)

    def test_julian_date_to_utc(self):
        self.assertEqual(self.calc.julian_date_to_utc(2440587.5), datetime(1970, 1, 1))
        self.assertEqual(self.calc.julian_date_to_utc(2451545.0), datetime(2000, 1, 1, 12))

    def test_calculate_celestial_position(self):
        result = self.calc.calculate_celestial_position(0, 0, 0, 0)
        self.assertEqual(result, {"azimuth": 0.0, "altitude": 0.0})

    def test_convert_equatorial_to_horizontal(self):
        result = self.calc.convert_equatorial_to_horizontal(0, 0, 0, 0, datetime.now())
        self.assertEqual(result, {"azimuth": 0.0, "altitude": 0.0})

if __name__ == '__main__':
    unittest.main()
```