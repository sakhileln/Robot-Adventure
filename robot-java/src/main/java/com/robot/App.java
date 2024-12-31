package com.robot;

import com.robot.Robot;
import com.robot.RacingRobot;
import com.robot.BattleBot;

import java.awt.geom.Point2D;

public class App 
{
    public static void main( String[] args )
    {
        /* Driver function for program. */
        Point2D.Double pos1 = new Point2D.Double(0,0);
        Robot robot1 = new Robot("C-P30", pos1, 0);
        Point2D.Double pos2 = new Point2D.Double(5.1, 5.0);
        RacingRobot racing_robot = new RacingRobot("SpeedBot", pos2, 45);
        Point2D.Double pos3 = new Point2D.Double(10.0, 10);
        BattleBot battle_bot = new BattleBot("CombatBot", pos3, 180);

        /* Test methods */
        robot1.move_forward(5);
        robot1.turn_left(90);
        robot1.talk("I'm a basic robot");

        racing_robot.move_forward(3);

        battle_bot.attack();
        battle_bot.talk("Prepare to fight!");

        /* Test static methods */
        Robot default_robot = Robot.create_default_robot();
        System.out.println(default_robot.toString());

        double distance = Robot.calculateDistance(robot1, battle_bot);
        System.out.print("Distance between Robot1 and Battlebot: ");
        System.out.println(distance);
    }
}
