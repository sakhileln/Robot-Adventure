package com.robot;

import java.awt.geom.Point2D;

public class BattleBot extends Robot {
    public BattleBot(String name, Point2D.Double position, double facing) {
        super(name, position, facing);
    }

    void attack() { System.out.println(robotName + " is attacking with laser beams!"); }
    @Override
    void talk(String message) { System.out.println("BattleBot " + robotName + " says: " + message); }
}
