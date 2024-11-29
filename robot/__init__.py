"""
robot package
-------------

This package provides functionalities related to robot operations. It includes modules for 
robot movement, turning, and communication. The core module 'robot' is imported here for 
ease of use.

Modules available:
- robot: Contains the main robot functionality such as movement, and turning.

The following functions and classes are available:
- RobotBase: Abstract Base Class that represents a robot with capabilities.
- Robot: Class to control robot movements (e.g., forward, backward, rotation).
- RacingRobot: Class that overrides Robot to make it faster.
- BattleBot: Class add attack functionality the robot.

This file ensures that the robot package is initialized correctly when imported.
"""
from robot.robot import *
