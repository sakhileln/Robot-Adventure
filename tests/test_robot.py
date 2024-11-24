import unittest
from unittest.mock import patch
from robot import Robot, RacingRobot, BattleBot


class TestRobot(unittest.TestCase):
    def test_robot_initialization(self):
        """Test the creation and initialization of a Robot."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        self.assertEqual(robot.name, "CP3O")
        self.assertEqual(robot.get_position(), (0, 0))
        self.assertEqual(robot._Robot__facing, 90)

    def test_move_forward(self):
        """Test Robot moving forward."""
        robot = Robot(name="CP3O", position=(0, 0), facing=0)
        robot.move_forward(5)
        self.assertEqual(robot.get_position(), (0, 5))
        self.assertEqual(robot._Robot__facing, 0)

    def test_turn_left(self):
        """Test turning robot to the left."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_left(90)
        self.assertEqual(robot._Robot__facing, 180)

    def test_turn_right(self):
        """Test turning robot to the right."""
        robot = Robot(name="CP3O", position=(0, 0), facing=90)
        robot.turn_right(90)
        self.assertEqual(robot._Robot__facing, 0)

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

    def test_calculate_distance(self):
        robot1 = Robot(name="C-P3O", position=(0, 0), facing=90)
        robot2 = Robot(name="R2-D2", position=(3, 4), facing=180)
        distance = Robot.calculate_distance(robot1, robot2)
        self.assertEqual(round(distance, 2), 5.0)


class TestRacingRobot(unittest.TestCase):
    def test_racing_robot_move(self):
        """Test RacingRobot moving forward"""
        racing_robot = RacingRobot(name="SpeedBot", position=(0, 0), facing=0)
        racing_robot.move_forward(3)
        self.assertEqual(racing_robot.get_position(), (0, 6))


class TestBattleBot(unittest.TestCase):
    """Test BattleBot attacking."""

    def test_battle_bot_attack(self):
        battle_bot = BattleBot(name="CombatBot", position=(0, 0), facing=180)
        with patch("builtins.print") as mock_print:
            battle_bot.attack()
            mock_print.assert_called_with(
                "CombatBot is attacking with laser beams!"
            )

    def test_battle_bot_talk(self):
        battle_bot = BattleBot(name="CombatBot", position=(0, 0), facing=180)
        with patch("builtins.print") as mock_print:
            battle_bot.talk("Prepare for battle!")
            mock_print.assert_called_with(
                "BattleBot CombatBot says: Prepare for battle!"
            )


if __name__ == "__main__":
    unittest.main()
