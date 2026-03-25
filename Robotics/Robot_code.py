from robodk.robolink import *

#connect to RoboDK
RDK = Robolink()

#Get robot
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.valid():
    raise Exception("Robot not found")

