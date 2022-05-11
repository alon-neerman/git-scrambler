#Test program wiith basic command line interaction
import RPi.GPIO as GPIO          
from time import sleep
#need to change these based on Rasp PI connections
in1 = 23
in2 = 24
ena = 25

in3 = 12
in4 = 13
enb = 15


#Motor 1 assuming right motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
#Starting at low, motor is stopped
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

#Motor 2, assuming left

#Starting at low, motor is stopped
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

frequency = 1000;
p=GPIO.PWM(ena,frequency)
p2= GPIO.PWM(enb,frequency)
#default duty cycle 25
duty_cycle = 25
#Steps size for increasing duty cycle
step_size = 5
p.start(duty_cycle)
p2.start(duty_cycle)
print("Default speed is dc 25.")
print("Options: ")
print("\n")    
print("F to move forward\nB to move backwards\nL to move left\nR to move right\nS to stop\nI to increase speed\nD to decrease speed\nE to exit")
while(1):

    x=input()
    
    if x=='f':
        print("Move Forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    elif x=='b':
        print("Move Backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.High)
        GPIO.output(in4,GPIO.High)
 
    elif x=='l':
    	#Move right motor forward and stop left motor
        print("Moving Left")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)

    elif x=='r':
    	#Moving left motor forward but stop the right
        print("Moving right")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
  
    elif x=='s':
        print("Stopping the robot")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
   

    elif x=='i':
        print("Increasing speed")
        duty_cylcle = duty_cycle + step_size
        p.ChangeDutyCycle(duty_cycle)
	p2.ChangeDutyCycle(duty_cycle)

    elif x=='d':
        print("Decreasing speed")
        duty_cylcle = duty_cycle - step_size
        p.ChangeDutyCycle(duty_cycle)
    	p2.ChangeDutyCycle(duty_cycle)
    elif x=='e':
        print("exitting")
        GPIO.cleanup()
        break
