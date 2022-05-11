#import RPi.GPIO as GPIO          
from time import sleep
import sys
from Sensors.IMU import IMU
from PLC import PLC

# Not sure how to implement PWM frequency.
class move_robot:
    #initialize
    # Speed is not absolute, its a value between 0-100 where 1000 is the max speed 
    # Threshold is for rotation accuracy, ie, how close to the desired angle are we allowed to reach
    def __init__(self, client, in1, in2, ena_pwm, in3, in4, enb_pwm, speed, IMU, threshold):
        self.in1 = in1
        self.in2 = in2
        self.ena_pwm = ena_pwm
        self.in3 = in3
        self.in4 = in4
        self.enb_pwm = enb_pwm
        self.speed = speed
        self.client = client
        self.IMU = IMU
        self.threshold = threshold
        self.start_heading = self.IMU.getHeading()
        #set in1-in4 to low. Robot is stopped by default
        self.client.write_digital_output(in1, 0)
        self.client.write_digital_output(in2, 0)
        self.client.write_digital_output(in3, 0)
        self.client.write_digital_output(in4, 0)
        #set speed to 0
        self.client.write_analog_output(ena_pwm, 0)
        self.client.write_analog_output(enb_pwm, 0)
        #io_value is 0 or 1 
        #client.write_digital_output(int(IO_Port), IO_Value)
        #client.write_analog_output()
    

    #Start robot motion.
    # If forward is 1 robot moves forward. If its 0, robot moves backward
    def startMotion(self, forward):
        #Robot moving forward
        if forward==1:
            #set in1 and in3 to High
            self.client.write_digital_output(in1, 1)
            self.client.write_digital_output(in3, 1)
            #Set in2 and in4 to low
            self.client.write_digital_output(in2, 0)
            self.client.write_digital_output(in4, 0)
            self.client.write_analog_output(ena_pwm, speed)
            self.client.write_analog_output(enb_pwm, speed)
        #Robot moving backward
        elif forward==0:
            #set in1 and in3 to Low
            self.client.write_digital_output(in1, 0)
            self.client.write_digital_output(in3, 0)
            #Set in2 and in4 to High
            self.client.write_digital_output(in2, 1)
            self.client.write_digital_output(in4, 1)
            self.client.write_analog_output(ena_pwm, speed)
            self.client.write_analog_output(enb_pwm, speed)

    #Stops robot motion
    def stopMotion(self):
        #set in1-in4 to low
        self.client.write_digital_output(in1, 0)
        self.client.write_digital_output(in2, 0)
        self.client.write_digital_output(in3, 0)
        self.client.write_digital_output(in4, 0)
        #set speed to 0 as well
        self.client.write_analog_output(ena_pwm, 0)
        self.client.write_analog_output(enb_pwm, 0)

    #Rotate robot, angle in degrees. Assume that starting angle is 0.
    def rotateRobot(self, angle):
        #angle is starting heading + desired angle
        rotate_angle = angle + self.start_heading
        #move right to increase angle and left to decrease
        if (rotate_angle > start_heading):
            angle_reached = False
            while(angle_reached != True):
                #keep rotating right motor
                #Set in3 to true. Move only left motor forward and stop right motor
                self.client.write_digital_output(in1, 0)
                self.client.write_digital_output(in2, 0)
                self.client.write_digital_output(in3, 1)
                self.client.write_digital_output(in4, 0)
                self.client.write_analog_output(ena_pwm, 0)
                self.client.write_analog_output(enb_pwm, self.speed)
                if (-threshold < (self.IMU.getHeading() - angle) < threshold):
                    angle_reached = True

        elif (rotate_angle < start_heading):
            angle_reached = False
            while(angle_reached != True):
                #keep rotating left
                #Set in1 to true. Move only right motor forward and stop left motor
                self.client.write_digital_output(in1, 1)
                self.client.write_digital_output(in2, 0)
                self.client.write_digital_output(in3, 0)
                self.client.write_digital_output(in4, 0)
                self.client.write_analog_output(ena_pwm, self.speed)
                self.client.write_analog_output(enb_pwm, 0)
                if (-threshold <= (self.IMU.getHeading() - angle) <= threshold):
                    angle_reached = True

    #Changes speed. Speed is not absolute, need value from 0 - 1000
    def changeSpeed(self, speed):
        self.speed = speed
        self.client.write_analog_output(ena_pwm, self.speed)
        self.client.write_analog_output(enb_pwm, self.speed)