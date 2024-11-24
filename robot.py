from abc import ABC, abstractmethod


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
    def __init__(self, name: str, position: tuple = (0, 0), facing: int = 0):
        self.name = name
        self.__position = position
        self.__facing = facing
