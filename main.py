from robot import Robot, RacingRobot, BattleBot


def main():
    # Create instances
    robot1 = Robot(name="C-P3O", position=(0, 0), facing=0)
    racing_robot = RacingRobot(name="SpeedBot", position=(5, 5), facing=45)
    battle_bot = BattleBot(name="CombatBot", position=(10, 10), facing=180)

    # Test methods
    print(robot1)


if __name__ == "__main__":
    main()
