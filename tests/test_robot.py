import unittest
from unittest.mock import patch
from robot import Robot

class TestRobot(unittest.TestCase):
    def test_robot_initialization(self):
        """Test the creation and initialization of a Robot."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        self.assertEqual(robot.name, "CP3O")
        self.assertEqual(robot.get_position(), (0, 0))
        self.assertEqual(
            robot._Robot__facing, 90
        )

    def test_move_forward(self):
        """Test Robot moving forward."""
        robot = Robot(name="CP3O", position=(0, 0), facing=0)
        robot.move_forward(5)
        self.assertEqual(
            robot.get_position(), (0, 5)
        )
        self.assertEqual(
            robot._Robot__facing, 0
        )

    def test_turn_left(self):
        """Test turning robot to the left."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_left(90)
        self.assertEqual(
            robot._Robot__facing, 180
        )

    def test_turn_right(self):
        """Test turning robot to the right."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_right(90)
        self.assertEqual(
            robot._Robot__facing, 0
        )

    def test_talk(self):
        """Test talking functionality."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        with patch("builtins.print") as mock_print:
            robot.talk("Hello")
            mock_print.assert_called_with("CP3O says: Hello")

    def test_create_default_robot(self):
        """Test Class Method (create_default_robot"""
        robot = Robot.create_default_robot()
        self.assertEqual(robot.name, "DefaultRobot")
        self.assertEqual(robot.get_position(), (0, 0))
        self.assertEqual(robot._Robot__facing, 0)

if __name__ == "__main__":
    unittest.main()
