from robot import Robot, RacingRobot, BattleBot


def main():
    # Create instances
    robot1 = Robot(name="C-P3O", position=(0, 0), facing=0)
    racing_robot = RacingRobot(name="SpeedBot", position=(5, 5), facing=45)
    battle_bot = BattleBot(name="CombatBot", position=(10, 10), facing=180)

    # Test methods
    print(robot1)
    robot1.move_forward(5)
    robot1.turn_right(90)
    robot1.talk("I'm a basic robot.")

    print(racing_robot)
    racing_robot.move_forward(3)

    print(battle_bot)
    battle_bot.attack()
    battle_bot.talk("Prepare to fight!")

    # Test class methods and static methods
    default_robot = Robot.create_default_robot()
    print(f"Created {default_robot}")

    distance = Robot.calculate_distance(robot1, battle_bot)
    print(f"Distance between Robo1 and CombatBot: {distance:.2f} meters.")


if __name__ == "__main__":
    main()
