package com.robot;

public abstract class RobotBase {
    abstract void move_forward(double distance);
    abstract void turn_left(double degrees);
    abstract void turn_right(double degrees);
    abstract void talk(String message);
}
