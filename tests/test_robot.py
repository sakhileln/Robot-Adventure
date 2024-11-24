import unittest
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
            robot.get_position(), (5, 0)
        )
        self.assertEqual(
            robot._Robot__facing, 0
        )

if __name__ == "__main__":
    unittest.main()
