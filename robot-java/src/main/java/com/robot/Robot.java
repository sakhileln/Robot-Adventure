package com.robot;

public class Robot {
    public abstract class RobotBase {
        abstract void move_forward(int distance);
        abstract void turn_left(int degrees);
        abstract void turn_right(int degrees);
        abstract String talk(String message);
    }
}
