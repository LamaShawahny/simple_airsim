from unittest import TestCase
from Algorithm.DroneAlgoInterface import DroneAlgoInterface
from simple_airsim.api.drone import Drone


class TestDroneAlgoInterface(TestCase):

    def test_loop(self) ->str:

        MyDrone = DroneAlgoInterface(0.3, 1, 0.25, 2.5)

        resulturnCW = MyDrone.loop(Drone, 6.34653425216676, 2.2126037273273407, 2.73489475250248)
        print("resulturnCW: " + resulturnCW)
        self.assertEqual(resulturnCW, "Turn_CW")

        resultEme = MyDrone.loop(Drone, 0.20487928390508, 2.2126037273273407, 2.73489475250248)
        print("resultEme: " + resultEme)
        self.assertEqual(resultEme, "Emergency")

        resultun = MyDrone.loop(Drone, 6.34653425216678, 0.20487928390508, 0.234475250248)
        print("resultun: " + resultun)
        self.assertEqual(resultun, "Tunnel")

        ## Test case 1
        result1 = MyDrone.loop(Drone, 6.34653425216676, 2.2126037273273407, 2.73489475250248)
        print("Result1: " + result1)
        self.assertEqual(result1, "Turn_CW")

        ## Test case 2 ##
        result2 = MyDrone.loop(Drone, 1.9, 0.358423114, 0.672449708)
        print("Result2: " + result2)
        self.assertEqual(result2, "FlyForward")

        ## Test case 3 ##
        result3 = MyDrone.loop(Drone, 0.812300443649294, 0.20487928390508, 0.830004870891593)
        print("Result3: " + result3)
        self.assertEqual(result3, "Rotate_CCW")

        ## Test case 4 ##
        result4 = MyDrone.loop(Drone, 6.34653425216676, 2.2126037273273407, 2.73489475250248)
        print("Result4: " + result4)
        self.assertEqual(result4, "Turn_CW")

        ## Test case 5 ##
        result5 = MyDrone.loop(Drone, 1.9, 0.358423114, 0.672449708)
        print("Result5: " + result5)
        self.assertEqual(result5, "FlyForward")

        ## Test case 6 ##
        result6 = MyDrone.loop(Drone, 0.84348, 0.7523, 0.68732)
        print("Result6: " + result6)
        self.assertEqual(result6, "Rotate_CCW")

        ## Test case 7 ##
        result7 = MyDrone.loop(Drone, 2.623, 4.3783, 0.89239)
        print("Result7: " + result7)
        self.assertNotEquals(result7, "Rotate_CCW")

        ## Test case 8 ##
        result8 = MyDrone.loop(Drone, 9.8634843, 0.76238324, 0.572357)
        print("Result8: " + result8)
        self.assertNotEquals(result8, "Turn_CW")
