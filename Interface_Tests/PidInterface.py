class PidInterface:
    """This abstract class represents an interface PID function."""

    def __init__(self, p=0, i=0, d=0, n=1, invalid=-1):
        """
        Initialization for the PID function.
        """
        self.kP = p
        self.kI = i
        self.kD = d
        self._error_prior = 0
        self._integral_prior = 0
        self.ans = 0
        self.target = n
        self.min = -1000000
        self.max = 1000000
        self.last_time = 0
        self.__derivative_prior = 0  # # for debug only !
        self.dt = 0.1
        self.invalid = -1

    def __str__(self) -> str:
        """
        Returns a string which represents the  PID function
        @return: PID equation (string)
        """

    def set_bounds(self, min: int, max: int):
        """Modifying boundres
        """

    def reset(self):
        """resetting other elements
        """

    def constrain(slef, angel, min, max):
        """constrain
        """

    def update_dt(self, now):
        """update_dt
        """

    def pid(self, curr, now) -> None:
        """
            PID function implementation and getting result
            @param curr:
            @param now:
            @return: the answer of the PID function
        """
        if curr == None or curr == self.invalid or curr < 0:
            return 0
        error = curr - self.target
        derivative = (error - self._error_prior) / self.dt
        integral = self._integral_prior + error * self.dt
        self._error_prior = error
        self._integral_prior = integral
        self.__derivative_prior = derivative

        ans = (error * self.kP + derivative * self.kD + integral * self.kI)
        ans = self.constrain(ans, self.min, self.max)
        return ans
