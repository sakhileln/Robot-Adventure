"""
Unit tests for the `Robot`, `RacingRobot`, and `BattleBot` classes.

This module contains test cases that verify the functionality of the Robot-related
classes, including movement, turning, talking, distance calculation, and the
specialized behavior of RacingRobot and BattleBot subclasses. The tests use the
`unittest` framework to ensure that the methods and attributes of the classes
are working as expected.

Tested classes:
- Robot: Basic robot functionality.
- RacingRobot: Subclass of Robot with enhanced movement speed.
- BattleBot: Subclass of Robot with attack and specialized talking functionality.

Mocking is used for testing the `talk` method to verify the printed output.
"""

import unittest
from unittest.mock import patch
from robot import Robot, RacingRobot, BattleBot  # Absolute import


class TestRobot(unittest.TestCase):
    """Test cases for the Robot class."""

    def test_robot_initialization(self):
        """Test the creation and initialization of a Robot."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        self.assertEqual(robot.name, "CP3O")
        self.assertEqual(robot.get_position(), (0, 0))
        self.assertEqual(robot.get_facing(), 90)  # Use getter for __facing

    def test_move_forward(self):
        """Test the Robot's move_forward method."""
        robot = Robot(name="CP3O", position=(0, 0), facing=0)
        robot.move_forward(5)
        self.assertEqual(robot.get_position(), (0, 5))
        self.assertEqual(robot.get_facing(), 0)  # Use getter for __facing

    def test_turn_left(self):
        """Test the Robot's turn_left method."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_left(90)
        self.assertEqual(robot.get_facing(), 180)  # Use getter for __facing

    def test_turn_right(self):
        """Test the Robot's turn_right method."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_right(90)
        self.assertEqual(robot.get_facing(), 0)  # Use getter for __facing

    def test_talk(self):
        """Test the Robot's talk method."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        with patch("builtins.print") as mock_print:
            robot.talk("Hello")
            mock_print.assert_called_with("CP3O says: Hello")

    def test_create_default_robot(self):
        """Test the create_default_robot class method."""
        robot = Robot.create_default_robot()
        self.assertEqual(robot.name, "DefaultRobot")
        self.assertEqual(robot.get_position(), (0, 0))
        self.assertEqual(robot.get_facing(), 0)  # Use getter for __facing

    def test_calculate_distance(self):
        """Test the calculate_distance static method."""
        robot1 = Robot(name="C-P3O", position=(0, 0), facing=90)
        robot2 = Robot(name="R2-D2", position=(3, 4), facing=180)
        distance = Robot.calculate_distance(robot1, robot2)
        self.assertEqual(round(distance, 2), 5.0)


class TestRacingRobot(unittest.TestCase):
    """Test cases for the RacingRobot subclass."""

    def test_racing_robot_move(self):
        """Test the RacingRobot's move_forward method with higher speed."""
        racing_robot = RacingRobot(name="SpeedBot", position=(0, 0), facing=0)
        racing_robot.move_forward(3)
        self.assertEqual(racing_robot.get_position(), (0, 6))


class TestBattleBot(unittest.TestCase):
    """Test cases for the BattleBot subclass."""

    def test_battle_bot_attack(self):
        """Test the BattleBot's attack method."""
        battle_bot = BattleBot(name="CombatBot", position=(0, 0), facing=180)
        with patch("builtins.print") as mock_print:
            battle_bot.attack()
            mock_print.assert_called_with("CombatBot is attacking with laser beams!")

    def test_battle_bot_talk(self):
        """Test the BattleBot's talk method."""
        battle_bot = BattleBot(name="CombatBot", position=(0, 0), facing=180)
        with patch("builtins.print") as mock_print:
            battle_bot.talk("Prepare for battle!")
            mock_print.assert_called_with(
                "BattleBot CombatBot says: Prepare for battle!"
            )


if __name__ == "__main__":
    unittest.main()
