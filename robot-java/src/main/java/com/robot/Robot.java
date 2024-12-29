package com.robot;

import com.robot.RobotBase;
import java.lang.Math;

class Robot extends RobotBase {
    // Fields
    String robotName;
    private double robotPosition;
    private int robotFacing;
    // Constructor
    public Robot(String name, double position, int facing) {
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
        // Update position with new (x + dx, y + dy)
        System.out.println(robotName + " moved forward by " + distance + " meters to " + "update position");
    }

}
