#POSITION CONTROL MOVE BACKWARD BY 0.2m
#POSITION CONTROL=VELOCITY FIXED, POSITION VARIES
from controller import Robot
robot=Robot()
TIME_STEP=int(robot.getBasicTimeStep())
WHEEL_RADIUS=0.035
TARGET_DISTANCE=-0.2
FIXED_SPEED=3.0
left_motor=robot.getMotor("motor_1")
right_motor=robot.getMotor("motor_2")
wheel_rotation=TARGET_DISTANCE/WHEEL_RADIUS
left_motor.setPosition(wheel_rotation)
right_motor.setPosition(wheel_rotation)
left_motor.setVelocity(FIXED_SPEED)
right_motor.setVelocity(FIXED_SPEED)
while robot.step(TIME_STEP)!=-1:
 pass
