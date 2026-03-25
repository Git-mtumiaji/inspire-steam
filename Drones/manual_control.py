from pysimverse import Drone
import time
import cv2
import keyboard
import pynput

drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(100)
rc_speed = 250

while True:
    #key = cv2.waitKey(1) & 0xff
    key = keyboard.read_key()

# Get all values to 0
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if key == ord("w"):
        forward_backward = rc_speed
    elif key == ord("s"):
        forward_backward = -rc_speed
    elif key == ord("a"):
        left_right = -rc_speed
    elif key == ord("d"):
        left_right = rc_speed
    elif key == ord("f"):
        up_down = rc_speed
    elif key == ord("c"):
        up_down = -rc_speed
    elif key == ord("q"):
        yaw = -1
    elif key == ord("e"):
        yaw = 1
    elif key == ord("l"):
        drone.land()
        time.sleep(2)
        break
    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )

