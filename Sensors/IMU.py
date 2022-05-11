import time
import board
import busio
import adafruit_lsm9ds1
import math
# This class is responsible for representing the IMU and allows for the functionality to get the reading whenever they are called.
# it uses this library: https://github.com/adafruit/Adafruit_CircuitPython_LSM9DS1
# Note that the library itself has dependancies we made need to install on the pi
class IMU:
     # init method or constructor    
    def __init__(self):   
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

    # returns a touple of values x acceleration, y acceleration, z acceleration. 
    # values are in (m/s^2)
    def getAccel(self): 
        accel_x, accel_y, accel_z = self.sensor.acceleration
        return (accel_x, accel_y, accel_z)

    # returns a touple of values x magnetometer, y magnetometer, z magnetometer
    # values are in gauss
    def getMag(self):    
        mag_x, mag_y, mag_z = self.sensor.magnetic
        return (mag_x, mag_y, mag_z)


    # returns a touple of values x gyro, y gyro, z gyro. 
    # values are in (degrees/sec)
    def getGyro(self):
        gyro_x, gyro_y, gyro_z = self.sensor.gyro
        return (gyro_x, gyro_y, gyro_z)

    # returns the temperature reading
    # values are in C
    def getTemp(self):
        temp = self.sensor.temperature
        return temp

    # returns heading calculated from magnetometer values
    def getHeading(self):
        # check if mag_x is 0. If it is  then check y. If y<0 then direction is 90 degrees.
        # if not, then direction is 0
        # if mag_x > 0 then arctan(mag_y/mag_x)
        mag_x, mag_y, mag_z = self.sensor.magnetic
        if (mag_x == 0):
            if (mag_y < 0):
                direction = 90
            else:
                direction = 0
        else:
            direction = arctan(mag_y/mag_x) * (180/math.pi)
        
        return direction

# saving this as formatting might be useful in gui

    # # Print values.
    # print(
    #     "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
    #         accel_x, accel_y, accel_z
    #     )
    # )
    # print(
    #     "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z)
    # )
    # print(
    #     "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
    #         gyro_x, gyro_y, gyro_z
    #     )
    # )
    # print("Temperature: {0:0.3f}C".format(temp))