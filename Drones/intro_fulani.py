from pysimverse import Drone
import time

# an instance of drone 
drone = Drone()
drone.connect()

drone.take_off()
# distance is in cm

drone.move_forward(250)
time.sleep(1)
drone.move_backward(250)
time.sleep(1)
drone.move_left(250)
time.sleep(1)
drone.move_right(250) 
time.sleep(1)

drone.land()