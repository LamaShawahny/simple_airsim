from unittest import TestCase
from Algorithm.PidInterface import PidInterface

class TestPidInterface(TestCase):
    def test_pid(self):
        prd = PidInterface()
        self.assertIsNone(prd.pid(0.004, 0.2332))
