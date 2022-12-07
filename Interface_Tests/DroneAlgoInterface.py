from simple_airsim.api.drone import Drone

"""
Article : Vision-Less Sensing for Autonomous Micro-Drones -2018
By: Simon Pikalov,Elisha Azaria ,Shaya Sonnenberg,Boaz Ben-Moshe andAmos Azaria

 Interface  or headlines for Drone Algorithm.
 Programmer : Lama Shawahny
"""


class DroneAlgoInterface:

    def __init__(self, emergency_threshold, front_threshold, tunnel_threshold, right_far_threshold):
        """
        Initialization for the drone parameters .
        """
        self.emergency_threshold = emergency_threshold
        self.front_threshold = front_threshold
        self.tunnel_threshold = tunnel_threshold
        self.right_far_threshold = right_far_threshold

    def Rotate_CCW(self) -> str:
        """
        Rotate C.C.W :slightly rotates counterclockwise(to align with the right wall).
        """
        return "Rotate_CCW"

    def Emergency(self) -> str:
        """
        Emergency state : Drone brakes to avoid crashing
        """
        return "Emergency"

    def Tunnel(self) -> str:
        """
        Tunnel :Drone centers in between the left and right walls while maintaining the
        desired speed.
        """
        return "Tunnel"

    def Turn_CW(self) -> str:
        """
        Turn_CW: Drone turns 90 degrees clockwise (to find the right wall)
        """
        return "Turn_CW"

    def FlyForward(self) -> str:
        """FlyForward: Drone flies forward while making minor adjustments to maintain
            predefined bounds, i.e., its distance from the right and the desired speed.
        """
        return "FlyForward"

    def loop(self, drone: Drone, front, left, right) -> str:
        """The main algorithm for drone ,
        Controlling algorithm in which drone states are represented here .
        """
        if front < self.emergency_threshold:
            return DroneAlgoInterface.Emergency(drone)
        elif front < self.front_threshold:
            return DroneAlgoInterface.Rotate_CCW(drone)
        elif left < self.tunnel_threshold and right < self.tunnel_threshold:
            return DroneAlgoInterface.Tunnel(drone)
        elif right > self.right_far_threshold:
            return DroneAlgoInterface.Turn_CW(drone)
        else:
            return DroneAlgoInterface.FlyForward(drone)
