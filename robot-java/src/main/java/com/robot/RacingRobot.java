package com.robot;

import java.awt.geom.Point2D;

public class RacingRobot extends Robot {
    // Inherit constructor from parent
    public RacingRobot(String name, Point2D.Double position, double facing) {
        super(name, position, facing);
    }
    @Override
    void move_forward(double distance) {
        /*Override move_forward method to make robot move twice as fast.*/
        super.move_forward(2 * distance);
    }
}
