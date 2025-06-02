#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
# AI Classification Classroom Element IDs
class ClassroomElements:
    BLUE_BALL = 0
    GREEN_BALL = 1
    RED_BALL = 2
    BLUE_RING = 3
    GREEN_RING = 4
    RED_RING = 5
    BLUE_CUBE = 6
    GREEN_CUBE = 7
    RED_CUBE = 8
# AI Vision Color Descriptions
ai_vision_11__Ball = Colordesc(1, 122, 183, 99, 10, 0.2)
ai_vision_11__Container = Colordesc(2, 171, 174, 102, 10, 0.2)
# AI Vision Code Descriptions
ai_vision_11 = AiVision(Ports.PORT11, ai_vision_11__Ball, ai_vision_11__Container, AiVision.ALL_TAGS, AiVision.ALL_AIOBJS)
motor_20 = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
#Project: Final Project
#Author: Orlando Cruz
#Date: 05/29/25
#Description: Drives forward to the balls scoops them up and drives to yellow container to drop them off
from vex import *


# Brain and devices
brain = Brain()
motor1 = Motor(Ports.PORT1)
motor2 = Motor(Ports.PORT2)
motor3 = Motor(Ports.PORT3)
vision_sensor = Vision(Ports.PORT10)




# Helper: Drive two motors forward
def drive_forward(m1, m2, speed=50):
    m1.spin(FORWARD, speed, PERCENT)
    m2.spin(FORWARD, speed, PERCENT)


# Helper: Stop all motors
def stop_all():
    motor1.stop()
    motor2.stop()
    motor3.stop()


# Step 1: Look for "ball"
brain.screen.print("Looking for ball...")
ball_found = vision_sensor.take_snapshot(ai_vision_11__Ball)


if vision_sensor.object_count > 0:
    brain.screen.print("Ball found. Driving motors 2 and 3 forward.")
    # Step 2: Drive motor2 and motor3 forward for 5 seconds
    drive_forward(motor2, motor3, 50)
    wait(5, SECONDS)
    motor2.stop()
    motor3.stop()


    # Step 3: Spin motor1 forward for 3 seconds
    motor1.spin(FORWARD, 50, PERCENT)
    wait(3, SECONDS)
    motor1.stop()


    # Step 4: Search for "container" with motor2 and motor3 spinning
    brain.screen.print("Looking for container...")
    motor2.spin(FORWARD, 30, PERCENT)
    motor3.spin(FORWARD, 30, PERCENT)
    while True:
        vision_sensor.take_snapshot(ai_vision_11__Container)
        if vision_sensor.object_count > 0:
            brain.screen.print("Container found.")
            break
        wait(0.1, SECONDS)


    # Step 5: Drive towards container for 5 seconds
    drive_forward(motor2, motor3, 50)
    wait(5, SECONDS)
    motor2.stop()
    motor3.stop()


    # Step 6: Move motor1 forward for 3 seconds
    motor1.spin(FORWARD, 50, PERCENT)
    wait(3, SECONDS)
    motor1.stop()
else:
    brain.screen.print("Ball not found.")
