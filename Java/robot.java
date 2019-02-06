/*----------------------------------------------------------------------------*/
/* Copyright (c) 2017-2018 FIRST. All Rights Reserved.                        */
/* Open Source Software - may be modified and shared by FRC teams. The code   */
/* must be accompanied by the FIRST BSD license file in the root directory of */
/* the project.                                                               */
/*----------------------------------------------------------------------------*/

package org.usfirst.frc.team6025.robot;

import edu.wpi.first.wpilibj.networktables.NetworkTable;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.Spark;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.command.Command;
import edu.wpi.first.wpilibj.drive.DifferentialDrive;
import edu.wpi.first.wpilibj.livewindow.LiveWindow;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;


public class Robot extends IterativeRobot {
	private Spark sagmotor1 = new Spark(0);
	private Spark sagmotor2 = new Spark(1);
	private Spark solmotor1 = new Spark(2);
	private Spark solmotor2 = new Spark(3);
	private Joystick m_stick = new Joystick(0);
	private Timer m_timer = new Timer();
	
	public static NetworkTable table1 = NetworkTable.getTable("Vision"); // vision adında table çekilioyr


	@Override
	public void robotInit() {
	}


	@Override
	public void autonomousInit() {
		m_timer.reset();
		m_timer.start();
	}
	
	public static double konumX()
	{
		return table1.getNumber("X", 0.0); //raspberry pi den gelen x kordinatları
	}
	public static double konumY() 
	{
		return table1.getNumber("Y", 0.0); //raspberry pi den gelen y kordinatları
	}


	@Override
	public void autonomousPeriodic() {
		if(konumX() < 285) // degerler 285'ten kucukse saga don
		{
			sagmotor1.set(1) // sag motorları calistir
			sagmotor2.set(1)
		}
	        else if (konumX() > 295) // degerler 295'ten buyukse sola don
		{
			solmotor1.set(1) //sol motorlari calistir
			solmotor2.set(1)
		}

	}

	@Override
	public void teleopInit() {
	}


	@Override
	public void teleopPeriodic() {
		SmartDashboard.putNumber("Nesnenin X konumu: ", konumX()); // smartdashboarda x konumu yazdır
		SmartDashboard.putNumber("Nesnenin Y konumu: ", konumY()); // smartdashboarda y konumunu yazdır

	}


	@Override
	public void testPeriodic() {
	}
}
