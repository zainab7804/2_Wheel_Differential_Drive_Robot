#CONTINUOUS FORWARD MOTION
from controller import Robot
#imports robot library
robot=Robot()
TIME_STEP=int(robot.getBasicTimeStep())
MAX_SPEED=6.20
left_motor=robot.getMotor("motor_1")
right_motor=robot.getMotor("motor_2")
left_motor.setPosition(float('inf'))
#setting position to infinity is called velocity control
right_motor.setPosition(float('inf'))
while robot.step(TIME_STEP)!=-1:
 left_motor.setVelocity(MAX_SPEED)
 right_motor.setVelocity(MAX_SPEED)
