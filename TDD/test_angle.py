
import unittest
from angle import Angle


class TestAngle(unittest.TestCase):
    def test_degrees(self):
        small_angle = Angle(60)
        self.assertEqual(60, small_angle.degrees)
        self.assertTrue(small_angle.is_acute())
        big_angle = Angle(320)
        self.assertFalse(big_angle.is_acute())
        funny_angle = Angle(1081)
        self.assertEqual(1, funny_angle.degrees)

    def test_arithmatic(self):
        small_aggle = Angle(60)
        big_angle = Angle(320)
        total_angle = small_aggle.add(big_angle)
        self.assertEqual(20, total_angle.degrees, 'Adding agle with wrap-around')

