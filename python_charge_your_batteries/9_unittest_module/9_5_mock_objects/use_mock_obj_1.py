import unittest
from random import randint
from unittest.mock import Mock


def get_speed():
    return randint(40, 120)


def is_speed_violation():
    speed = get_speed()
    if speed < 60 or speed > 100:
        return True
    return False


class TestSpeed(unittest.TestCase):
    def test_alert_normal(self):
        get_speed = Mock()
        get_speed.return_value = 70
        self.assertFalse(is_speed_violation())

    def test_alert_overspeed(self):
        get_speed = Mock()
        get_speed.return_value = 100
        self.assertFalse(is_speed_violation())

    def test_alert_underspeed(self):
        get_speed = Mock()
        get_speed.return_value = 59
        self.assertTrue(is_speed_violation())