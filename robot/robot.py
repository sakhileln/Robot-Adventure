"""
This module defines a hierarchy of robot classes, including an abstract base class
and specific implementations for a general Robot, a RacingRobot, and a BattleBot.

- RobotBase: Abstract base class that defines the common interface for all robots.
- Robot: A general robot class that implements the movement, turning, and talking behaviors.
- RacingRobot: A subclass of Robot that overrides movement to make the robot faster.
- BattleBot: A subclass of Robot with additional attack functionality and custom talking behavior.

This module allows the creation of robots that can move, turn, talk, and interact with each other.
"""

from abc import ABC, abstractmethod
from math import radians, cos, sin, sqrt


# Abstract Base Class
class RobotBase(ABC):
    """Abstract Base Class for all robots, defining common behavior."""

    @abstractmethod
    def move_forward(self, distance=1):
        """Move the robot forward by a given distance."""

    @abstractmethod
    def turn_left(self, degrees):
        """Turn the robot left by a given number of degrees."""

    @abstractmethod
    def turn_right(self, degrees):
        """Turn the robot right by a given number of degrees."""

    @abstractmethod
    def talk(self, message):
        """Make the robot say a given message."""


class Robot(RobotBase):
    """Main Robot Class that implements RobotBase and provides movement functionality."""

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
        """
        Get the current position of the robot.

        :return: The current position of the robot as a tuple (x, y).
        """
        return self.__position

    def set_position(self, new_position: tuple):
        """
        Set the position of the robot to a new value.

        :param new_position: The new position as a tuple (x, y).
        """
        self.__position = new_position

    def get_facing(self):
        """
        Returns the current facing direction of the robot.

        This method provides access to the robot's internal facing angle,
        which is represented as a degree value between 0 and 360.

        :return: The robot's facing direction in degrees (0-360).
        :rtype: int
        """
        return self.__facing

    def move_forward(self, distance: int = 1):
        """
        Move the robot forward by the specified distance.

        :param distance: The distance the robot should move forward (default is 1).
        """
        angle_rad = radians(self.__facing)
        dx = distance * sin(angle_rad)
        dy = distance * cos(angle_rad)
        x, y = self.__position
        self.__position = (x + dx, y + dy)
        print(f"{self.name} moved forward by {distance} meters to {self.__position}.")

    def turn_left(self, degrees: int):
        """
        Turn the robot left by the specified number of degrees.

        :param degrees: The number of degrees to turn the robot to the left.
        """
        self.__facing = (self.__facing + degrees) % 360
        print(
            f"{self.name} turned left by {degrees} degrees. Now facing {self.__facing} degrees."
        )

    def turn_right(self, degrees: int):
        """
        Turn the robot right by the specified number of degrees.

        :param degrees: The number of degrees to turn the robot to the right.
        """
        self.__facing = (self.__facing - degrees) % 360
        print(
            f"{self.name} turned right by {degrees} degrees. Now facing {self.__facing} degrees."
        )

    def talk(self, message: str):
        """
        Make the robot say the specified message.

        :param message: The message for the robot to say.
        """
        print(f"{self.name} says: {message}")

    @classmethod
    def create_default_robot(cls):
        """
        Create a default robot with predefined parameters
        (name='DefaultRobot', position=(0,0), facing=0).

        :return: A new instance of the Robot class with default parameters.
        """
        return cls(name="DefaultRobot", position=(0, 0), facing=0)

    @staticmethod
    def calculate_distance(robot1: "Robot", robot2: "Robot"):
        """
        Calculate the distance between two robots.

        :param robot1: The first robot.
        :param robot2: The second robot.
        :return: The distance between the two robots as a float.
        """
        x1, y1 = robot1.get_position()
        x2, y2 = robot2.get_position()
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def __str__(self) -> str:
        """
        Return a string representation of the robot, including its name,
        position, and facing direction.

        :return: A string describing the robot.
        """
        return f"My name is: {self.name}, I am at {self.__position}, facing {self.__facing}"


class RacingRobot(Robot):
    """Subclass of Robot that overrides movement to make it faster (polymorphism)."""

    def __init__(self, name: str, position: tuple = (0, 0), facing=0):
        """
        Initialize a RacingRobot instance, inheriting from the Robot class.

        :param name: The name of the racing robot.
        :param position: The initial position of the robot as a tuple (x, y).
        :param facing: The direction the robot is facing in degrees.
        """
        super().__init__(name, position, facing)

    def move_forward(self, distance: int = 2):
        """
        Override the move_forward method to make the robot move twice as fast.

        :param distance: The distance the robot should move forward (default is 2).
        """
        super().move_forward(2 * distance)  # Move twice as fast


class BattleBot(Robot):
    """Subclass of Robot for a BattleBot that adds attack functionality and custom talk behavior."""

    def __init__(
        self: "BattleBot", name: str, position: tuple = (0, 0), facing=0
    ) -> None:
        """
        Initialize a BattleBot instance, inheriting from the Robot class.

        :param name: The name of the battle bot.
        :param position: The initial position of the robot as a tuple (x, y).
        :param facing: The direction the robot is facing in degrees.
        """
        super().__init__(name, position, facing)

    def attack(self: "BattleBot") -> None:
        """
        Simulate an attack action by the battle bot.

        This method doesn't take any parameters and simply prints that the BattleBot is attacking.
        """
        print(f"{self.name} is attacking with laser beams!")

    def talk(self: "BattleBot", message: str) -> None:
        """
        Override the talk method to add a custom message for BattleBots.

        :param message: The message the BattleBot should say.
        """
        print(f"BattleBot {self.name} says: {message}")


if __name__ == "__main__":
    # Create an instance of RacingRobot and test its functionality
    racing_robot = RacingRobot(name="SpeedBot", position=(0, 0), facing=0)
    racing_robot.move_forward(3)
    pos = racing_robot.get_position()
