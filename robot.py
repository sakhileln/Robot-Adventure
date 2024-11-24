from abc import ABC, abstractmethod
from math import radians, cos, sin, sqrt


# Abstract Base Class
class RobotBase(ABC):
    @abstractmethod
    def move_forward(self, distance=1): ...
    @abstractmethod
    def turn_left(self, degrees): ...
    @abstractmethod
    def turn_right(self, degrees): ...
    @abstractmethod
    def talk(self, message): ...


class Robot(RobotBase):
    """Main Robot Class that implements RobotBase"""

    def __init__(self, name: str, position: tuple = (0, 0), facing: int = 0):
        """
        Initializes a new robot with a given name, position, and facing direction.

        :param name: The name of the robot.
        :param position: The initial position of the robot as (x, y).
        :param facing: The direction the robot is facing in degrees (0-360).
        """
        self.name = name
        self.__position = position
        self.__facing = facing

    def get_position(self):
        return self.__position

    def set_position(self, new_position: tuple):
        self.__position = new_position

    def move_forward(self, distance: int=1):
        angle_rad = radians(self.__facing)
        dx = distance * sin(angle_rad)
        dy = distance * cos(angle_rad)
        x, y = self.__position
        self.__position = (x + dx, y + dy)
        print(
            f"{self.name} moved forward by {distance} meters to {self.__position}."
        )

    def turn_left(self, degrees: int):
        self.__facing = (self.__facing + degrees) % 360
        print(
            f"{self.name} turned left by {degrees} degrees. Now facing {self.__facing} degrees."
        )

    def turn_right(self, degrees: int):
        self.__facing = (self.__facing - degrees) % 360
        print(
            f"{self.name} turned right by {degrees} degrees. Now facing {self.__facing} degrees."
        )

    def talk(self, message: str):
        print(f"{self.name} says: {message}")

    # Create dafault bot
    @classmethod
    def create_default_robot(cls):
        return cls(name="DefaultRobot", position=(0, 0), facing=0)

    # Static method (Disrance between two robots)
    @staticmethod
    def calculate_distance(robot1: "Robot", robot2: "Robot"):
        x1, y1 = robot1.get_position()
        x2, y2 = robot2.get_position()
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
