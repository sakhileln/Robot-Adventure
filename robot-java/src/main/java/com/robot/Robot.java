package com.robot;

import com.robot.RobotBase;
import java.lang.Math;
import java.awt.geom.Point2D;

class Robot extends RobotBase {
    // Fields
    String robotName;
    private Point2D.Double robotPosition;
    private double robotFacing;
    // Constructor
    public Robot(String name, Point2D.Double position, double facing) {
        this.robotName = name;
        this.robotPosition = position;
        this.robotFacing = facing;
    }
    /*
    Parameterless contructor
    Robot() {
    }
    */
    // Methods
    void setPosition(double x, double y) { robotPosition.setLocation(x, y); }

    double getFacing() { return robotFacing; }
    Point2D.Double getPosition() { return robotPosition; }

    void move_forward(double distance) {
        double angle_rad = Math.toRadians(robotFacing);
        double dx = distance * Math.sin(angle_rad);
        double dy = distance * Math.cos(angle_rad);
        // Extract (x,y) from position
        double x = robotPosition.getX();
        double y = robotPosition.getY();
        // Update position with new (x + dx, y + dy)
        robotPosition.setLocation(x + dx, y + dy);
        System.out.print(robotName + " moved forward by " + distance + " meters to ");
        System.out.println("(" + robotPosition.getX() + "," + robotPosition.getY() + ")");
    }

    void turn_left(double degrees) {
        robotFacing = (robotFacing + degrees) % 360;
        System.out.print(robotName + " turned right by " + degrees + " degrees. Now facing ");
        System.out.println(robotFacing + " degrees.");
    }
    void turn_right(double degrees) {
        robotFacing = (robotFacing - degrees) % 360;
        System.out.print(robotName + " turned left by " + degrees + " degrees. Now facing ");
        System.out.println(robotFacing + " degrees.");
    }
    void talk(String message) { System.out.println(robotName + " says " + message); }

    // Static method
    static double calculateDistance(Robot robot1, Robot robot2) {
        Point2D.Double p1 = robot1.robotPosition;
        Point2D.Double p2 = robot2.robotPosition;
        double x1 = p1.getX();
        double y1 = p1.getY();
        double x2 = p2.getX();
        double y2 = p2.getY();
        /* Calculate distance */
        return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
    }
    static Robot create_default_robot() {
        return new Robot("DefaultRobot", new Point2D.Double(0,0), 0);
    }

    @Override
    public String toString() {
        return "My name is: " +
                robotName +
                ", I am at " +
                "(" + robotPosition.getY() + "," + robotPosition.getY() + ")" +
                " facing " + robotFacing;
    }
}
