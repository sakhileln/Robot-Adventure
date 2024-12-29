package com.robot;

import com.robot.RobotBase;
import java.lang.Math;
import java.awt.geom.Point2D;

class Robot extends RobotBase {
    // Fields
    String robotName;
    private Point2D.Double robotPosition = new Point2D.Double(0, 0);
    private int robotFacing;
    // Constructor
    public Robot(String name, Point2D.Double position, int facing) {
        robotName = name;
        robotPosition = position;
        robotFacing = facing;
    }
    // Methods
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



}
